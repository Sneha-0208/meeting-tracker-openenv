import os
import requests
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://tensorflow123-meeting-tracker.hf.space")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

client = OpenAI(api_key=HF_TOKEN)

MAX_STEPS = 5


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


def main():

    task_name = "meeting"
    benchmark = "meeting_tracker"

    log_start(task_name, benchmark, MODEL_NAME)

    reset = requests.post(f"{API_BASE_URL}/reset").json()

    rewards = []
    done = False

    for step in range(1, MAX_STEPS + 1):

        action = {
            "action_type": "create",
            "description": "send report",
            "owner": "Rahul",
            "deadline": "Friday",
        }

        result = requests.post(f"{API_BASE_URL}/step", json=action).json()

        reward = result["reward"]
        done = result["done"]

        rewards.append(reward)

        log_step(step, str(action), reward, done)

        if done:
            break

    score = sum(rewards) / len(rewards) if rewards else 0
    success = score > 0.5

    log_end(success, len(rewards), score, rewards)


if __name__ == "__main__":
    main()