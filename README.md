#  DecepTron – AI-Powered Deception Honeypot

DecepTron is an intelligent AI-powered cybersecurity honeypot that uses a local Large Language Model (LLM) to simulate vulnerable network services. It is designed to attract, deceive, and analyze attackers in real time, providing valuable threat intelligence while running fully offline for maximum privacy.

---





#  🧑‍💻Features

AI-Powered Interaction → Uses a local Llama-3 model to generate realistic attacker responses.

Multi-Service Deception → Simulates an SSH-style terminal (port 2222).

Real-Time Logging → Captures attacker commands + AI responses into an SQLite database.

Live Analytics Dashboard → Streamlit web UI for real-time monitoring.

Fully Local & Private → Runs without any external APIs or cloud services.

----



# 🛠️ Tech Stack

Backend → Python 3, Sockets, Threading

AI Engine → llama-cpp-python
 with Llama 3 8B GGUF

Database → SQLite

Dashboard → Streamlit + Pandas

Attacker Clients → PuTTY (SSH/terminal)

---



# 📦 Installation

### 1️. Clone the repository
git clone https://github.com/Sagarchhetri83/DecepTron-AI-Honeypot.git
cd DecepTron-AI-Honeypot

### 2️. Create & activate virtual environment
-Create venv
python -m venv .venv  

-Activate on Windows
.\.venv\Scripts\activate

### 3️. Install dependencies
-pip install -r requirements.txt

### 4️. Download the AI Model

-Download Meta-Llama-3-8B-Instruct.Q4_K_M.gguf and place it in the /models directory.

-Update the MODEL_PATH variable in backend/offensive_ai.py to point to this file.

---

# ▶️ Usage

### -Run the system in multiple terminals:

-Terminal 1 – Dashboard

streamlit run dashboard.py


-Terminal 2 – Main Honeypot

python -m backend.app

---




# 🔗 Connect with:

### PuTTY → SSH honeypot on port 2222

All activity is logged into SQLite and visualized on the dashboard.

---




# 👨‍💻 Credits

Developed by Sagar Chhetri 
A hands-on project exploring offensive AI, deception, and cybersecurity research.

# 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.
