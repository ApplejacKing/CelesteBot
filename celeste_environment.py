from direct_keys import PressKey, ReleaseKey, W, A, S, D, ND1, ND2, ND3, Esc, Enter
import time
from actions import UP, LEFT, RIGHT, JUMP, DASH, action2key

SHORT = 0.1
MEDIUM = 0.3
LONG = 0.5

class CelesteEnvironment:
    """
    Class responsible for game environment and processing actions into the game.
    """

    def reset(self):
        """
        should restart current level in any case.
        """
        PressKey(Esc)
        time.sleep(SHORT)
        ReleaseKey(Esc)
        PressKey(S)
        time.sleep(SHORT)
        ReleaseKey(S)
        PressKey(Enter)
        time.sleep(SHORT)
        ReleaseKey(Enter)
        time.sleep(4)

    def do_actions(self, actions, sleep_time):
        for action in actions:
            PressKey(action2key[action])
        time.sleep(sleep_time)
        for action in actions:
            ReleaseKey(action2key[action])

if __name__ == "__main__":
    environment = CelesteEnvironment()
    time.sleep(3)
    environment.reset()
    environment.do_actions([JUMP], SHORT)
    time.sleep(LONG)
    environment.do_actions([RIGHT, UP, DASH], SHORT)
    time.sleep(4)
    environment.do_actions([JUMP], MEDIUM)
    environment.do_actions([RIGHT, UP, DASH], MEDIUM)
    environment.reset()
