DecepTron 🍯 - An AI-Powered Deception Honeypot
DecepTron is an intelligent cybersecurity honeypot system that leverages a local Large Language Model (LLM) to simulate vulnerable network services. It is designed to attract, deceive, and analyze attackers in real-time to gather valuable threat intelligence.

This project was developed as a hands-on exploration of offensive AI, network programming, and cybersecurity principles.

🚀 Features
Intelligent Attacker Interaction: Uses a local Llama 3 model to generate realistic and interactive terminal and FTP responses.

Multi-Service Deception: Simulates both a terminal (SSH-style on port 2222) and an FTP server (on port 21) to create a convincing decoy network.

Real-Time Logging: Records every attacker command and AI response to an SQLite database for analysis.

Live Analytics Dashboard: A web-based dashboard built with Streamlit to monitor all honeypot activity in real-time.

Fully Local & Private: Runs completely offline with no paid APIs, ensuring all data and interactions remain on your machine.

🛠️ Tech Stack
Backend: Python 3, Sockets, Threading

AI Engine: llama-cpp-python with the Llama 3 8B GGUF model

Database: SQLite

Dashboard: Streamlit & Pandas

Attacker Client: PuTTY (for terminal) & FileZilla (for FTP)

📦 Installation
Clone the repository:

git clone [https://github.com/Sagarchhetri83/DecepTron-AI-Honeypot.git](https://github.com/Sagarchhetri83/DecepTron-AI-Honeypot.git)
cd DecepTron-AI-Honeypot


Create and activate a virtual environment:

# Create the venv
python -m venv .venv
# Activate on Windows
.\.venv\Scripts\activate


Install dependencies:
(Note: llama-cpp-python may require C++ build tools to be installed on your system.)

pip install -r requirements.txt


Download the AI Model:
Download the Meta-Llama-3-8B-Instruct.Q4_K_M.gguf model and place it in the /models directory. Ensure the MODEL_PATH variable in backend/offensive_ai.py points to this file.

▶️ Usage
The system requires multiple separate terminals to run.

Run the Dashboard (Terminal 1):

streamlit run dashboard.py


Run the Main Honeypot (Terminal 2):

python -m backend.app


(Optional) Run the FTP Honeypot (Terminal 3):

python -m backend.ftp_honeypot


Connect to the honeypots using a client like PuTTY (for the main honeypot) or FileZilla (for the FTP honeypot) and observe the interactions on the dashboard.

📂 Project Structure
DecepTron/
│
├── backend/                # Core application logic
│   ├── __init__.py
│   ├── app.py              # Main terminal honeypot runner
│   ├── offensive_ai.py     # Handles LLM interaction
│   ├── logger.py           # Database logging functions
│   ├── defensive.py        # Threat detection logic
│   └── ftp_honeypot.py     # (Optional) FTP honeypot runner
│
├── data/                   # To store the SQLite database (ignored by git)
│
├── models/                 # To store large LLM files (ignored by git)
│
├── .gitignore              # Specifies files for git to ignore
├── dashboard.py            # The Streamlit dashboard application
├── requirements.txt        # Project dependencies for pip
└── README.md               # Project documentation

Credits
This project was created and developed by Sagar Chhetri.

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.