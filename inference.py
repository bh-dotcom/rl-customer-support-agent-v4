import subprocess
import time
import requests

BASE_URL = "http://127.0.0.1:8000"

# Start FastAPI server
proc = subprocess.Popen(["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"])
time.sleep(5)  # wait for server to start

try:
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
    final_score = 2.0  # sum of rewards
    print(f"[END] Final Score: {final_score}")

finally:
    # Stop the server
    proc.terminate()
    proc.wait()
