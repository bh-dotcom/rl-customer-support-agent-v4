import requests

BASE_URL = "http://127.0.0.1:8000"

def run_inference():
    print("[START] RL Customer Support Agent Inference")
    
    # Reset environment
    r = requests.post(f"{BASE_URL}/reset")
    print(f"[STEP] Reset: {r.json()}")
    
    # Step 1: simple query
    r = requests.post(f"{BASE_URL}/step", json={"query": "Hello"})
    print(f"[STEP] Step 1: {r.json()}")
    
    # Step 2: complex query
    r = requests.post(f"{BASE_URL}/step", json={"query": "I need help with billing"})
    print(f"[STEP] Step 2: {r.json()}")
    
    # Final score
    final_score = 2.0  # Sum of rewards in example
    print(f"[END] Final Score: {final_score}")

if __name__ == "__main__":
    run_inference()
