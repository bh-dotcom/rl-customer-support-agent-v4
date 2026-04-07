from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ----- Models -----
class Action(BaseModel):
    query: str

class Observation(BaseModel):
    state_text: str

# ----- Environment State -----
current_state = {"state_text": "Welcome to RL Customer Support Agent"}

# ----- OpenEnv API -----
@app.get("/state")
def state():
    return current_state

@app.post("/reset")
def reset():
    global current_state
    current_state = {"state_text": "Welcome to RL Customer Support Agent"}
    return current_state

@app.post("/step")
def step(action: Action):
    global current_state
    # Simple logic: echo the query
    current_state["state_text"] = f"Agent reply: {action.query}"
    reward = 1.0
    done = False
    info = {}
    return {"observation": current_state, "reward": reward, "done": done, "info": info}

# ----- Health Check -----
@app.get("/")
def health():
    return {"message": "RL Customer Support Agent Server Running"}

# ----- Main -----
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
