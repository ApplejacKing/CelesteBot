from actions import UP, LEFT, RIGHT, JUMP, DASH, action2key
import time


SHORT = 0.1
MEDIUM = 0.3
LONG = 0.5


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
        #self.environment.do_actions([JUMP], MEDIUM)
        #self.environment.do_actions([DASH], LONG)

        # self.environment.do_actions([JUMP], MEDIUM)
        # self.environment.hold([UP, RIGHT])
        # self.environment.do_actions([DASH], SHORT)
        # time.sleep(LONG)
        # self.environment.release([UP, RIGHT])
        self.environment.do_actions([JUMP], MEDIUM)
        self.environment.do_actions([DASH], LONG)
        self.environment.do_actions([JUMP], MEDIUM)
        self.environment.hold([UP, RIGHT])
        self.environment.do_actions([DASH], SHORT)
        #time necessary after dash
        time.sleep(LONG)
        #running on the third platform
        time.sleep(MEDIUM)
        #jump from the third to the forth platforms
        self.environment.do_actions([JUMP], MEDIUM)
        self.environment.do_actions([DASH], MEDIUM)
        time.sleep(SHORT)
        self.environment.release([UP, RIGHT])