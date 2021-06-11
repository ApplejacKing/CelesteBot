from direct_keys import PressKey, ReleaseKey, W, A, S, D, ND1, ND2, ND3, Esc, Enter
import time
from moves import UP, LEFT, RIGHT, JUMP, DASH, move2key
from constants import *


class CelesteEnvironment:
    """
    Class responsible for game environment and processing actions into the game.
    """

    def reset(self):
        """
        Should restart current level in any case.
        """
        PressKey(Esc)
        time.sleep(FRAME_TIME)
        ReleaseKey(Esc)
        PressKey(S)
        time.sleep(FRAME_TIME)
        ReleaseKey(S)
        PressKey(Enter)
        time.sleep(FRAME_TIME)
        ReleaseKey(Enter)
        time.sleep(4)

    def hold(self, action):
        PressKey(move2key[action])

    def release(self, action):
        ReleaseKey(move2key[action])
