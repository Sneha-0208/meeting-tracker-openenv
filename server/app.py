from fastapi import FastAPI
from .env import MeetingEnv
from .models import Action

app = FastAPI()
env = MeetingEnv()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/reset")
async def reset():
    obs = await env.reset()
    return {
        "observation": obs.model_dump(),
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.post("/step")
async def step(action: Action):
    obs, reward, done, info = await env.step(action)
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {
        "tasks": env.tasks,
        "step": env.step_count
    }


def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()