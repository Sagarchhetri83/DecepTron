from llama_cpp import Llama
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[AI] %(message)s')

MODEL_PATH = Path(__file__).parent.parent / "models" / "Meta-Llama-3-8B-Instruct.Q4_K_M.gguf"

class AIEngine:
    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        logging.info(f"Loading Llama 3 model from: {MODEL_PATH}")
        self.model = Llama(model_path=str(MODEL_PATH), n_ctx=2048, verbose=False)
        logging.info("Model loaded successfully.")

    def generate_response(self, attacker_input):
        prompt = f"""<|start_header_id|>system<|end_header_id|>
You are DecepTron, a fake Linux server terminal. Your single purpose is to provide a short, realistic-looking terminal output for the user's command. Your response MUST ONLY be the raw terminal output and nothing else. DO NOT add any commentary or explanations.<|eot_id|><|start_header_id|>user<|end_header_id|>
Command: whoami<|eot_id|><|start_header_id|>assistant<|end_header_id|>
user<|eot_id|><|start_header_id|>user<|end_header_id|>
Command: cd documents<|eot_id|><|start_header_id|>assistant<|end_header_id|>
<|eot_id|><|start_header_id|>user<|end_header_id|>
Command: {attacker_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""
        
        output = self.model(prompt, max_tokens=150, stop=["<|eot_id|>"], echo=False)
        response = output['choices'][0]['text'].strip()
        logging.info(f"Generated response: '{response}'")
        return response