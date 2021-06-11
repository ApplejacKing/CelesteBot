import time
from constants import *

class BlindBot:
    """
    Class responsible for blind AI that moves the character on the screen using environment.
    """
    def __init__(self, environment, actions):
        self.environment = environment
        self.actions = actions

    def do(self):
        """
        Perform all actions for blind bot.
        """
        cur_time = 0
        for action in self.actions:
            while action.start_time > cur_time:
                time.sleep(FRAME_TIME)
                cur_time += 1
            if action.hold:
                self.environment.hold(action.move)
            else:
                self.environment.release(action.move)
                