import socket
import threading
import logging
from .offensive_ai import AIEngine
from . import logger, defensive

HOST = '0.0.0.0'
PORT = 2222
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def handle_client(conn, addr, ai_engine):
    ip, port = addr
    logging.info(f"[+] Connection from {ip}:{port}")
    try:
        # Send the very first prompt
        conn.sendall(b"user@deceptron:~$ ")
        
        while True:
            data = conn.recv(1024)
            if not data: break
            
            attacker_command = data.decode('utf-8', errors='ignore').strip()
            if not attacker_command:
                conn.sendall(b"user@deceptron:~$ ")
                continue

            logging.info(f"[{ip}] CMD: '{attacker_command}'")
            ai_response = ai_engine.generate_response(attacker_command)
            
            # Send the AI's response
            conn.sendall(f"{ai_response}\n".encode('utf-8'))
            
            # --- SMART PROMPT LOGIC ---
            # Only send a new prompt if the AI's response doesn't already have one.
            if not ai_response.strip().endswith(('$', '~', '#', '>')):
                conn.sendall(b"user@deceptron:~$ ")
                
            logger.log_interaction(ip, port, attacker_command, ai_response)

    except ConnectionResetError:
        logging.warning(f"[!] Connection forcibly closed by {ip}")
    finally:
        logging.info(f"[-] Connection closed from {ip}:{port}")
        conn.close()

def start_honeypot():
    logging.info("Initializing AI Engine...")
    ai_engine = AIEngine()
    logger.initialize_database()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    logging.info(f"[*] DecepTron Honeypot is live on {HOST}:{PORT}")

    try:
        while True:
            # Set a 1-second timeout on the server
            server.settimeout(1.0)
            try:
                # This will now only block for 1 second before timing out
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr, ai_engine), daemon=True)
                thread.start()
            except socket.timeout:
                # This is expected. If no one connects, it will timeout.
                # The loop continues, which allows Python to listen for Ctrl+C.
                continue

    except KeyboardInterrupt:
        logging.info("\n[!] Shutdown signal received (Ctrl+C).")
    finally:
        logging.info("[!] Server shutdown complete.")
        server.close()

if __name__ == '__main__':
    start_honeypot()