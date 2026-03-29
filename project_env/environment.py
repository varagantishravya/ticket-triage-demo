from env.models import Observation, Action, Reward
from env.tasks import get_task
from env.grader import grade_action

class TicketEnv:
    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = get_task()
        self.done = False
        return Observation(**self.current_task)

    def step(self, action: Action):
        score, feedback = grade_action(self.current_task, action)

        reward = Reward(score=score, feedback=feedback)

        self.done = True

        return (
            Observation(**self.current_task),
            reward,
            self.done,
            {"feedback": feedback}
        )

    def state(self):
        return self.current_task