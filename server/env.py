from .models import Observation, Action, TaskItem
from .tasks import TASKS
from .graders import grade

class MeetingEnv:

    def __init__(self):
        self.step_count = 0
        self.tasks = []
        self.task_name = "easy"
        self.transcript = ""

    async def reset(self):
        self.step_count = 0
        self.tasks = []
        self.task_name = "easy"
        self.transcript = TASKS[self.task_name]["transcript"]

        return Observation(
            transcript=self.transcript,
            tasks=self.tasks,
            step=0,
            remaining_steps=10
        )

    async def step(self, action: Action):

        self.step_count += 1

        if action.action_type == "create":
            self.tasks.append(
                TaskItem(
                    description=action.description,
                    owner=action.owner,
                    deadline=action.deadline,
                    priority=action.priority
                )
            )

        expected = TASKS[self.task_name]["expected"]

        reward = grade(self.tasks, expected)

        done = self.step_count >= 5

        return Observation(
            transcript=self.transcript,
            tasks=self.tasks,
            step=self.step_count,
            remaining_steps=10 - self.step_count
        ), reward, done, {}