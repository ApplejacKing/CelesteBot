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

    def short_action(self, action):
        """
        should process AI actions into the game
        """
        PressKey(action2key[action])
        time.sleep(SHORT)
        ReleaseKey(action2key[action])

    def short_actions(self, actions):
        for action in actions:
            PressKey(action2key[action])
        time.sleep(SHORT)
        for action in actions:
            ReleaseKey(action2key[action])

    def medium_action(self, action):
        """
        should process AI actions into the game
        """
        PressKey(action2key[action])
        time.sleep(MEDIUM)
        ReleaseKey(action2key[action])

    def medium_actions(self, actions):
        for action in actions:
            PressKey(action2key[action])
        time.sleep(MEDIUM)
        for action in actions:
            ReleaseKey(action2key[action])

if __name__ == "__main__":
    environment = CelesteEnvironment()
    time.sleep(3)
    environment.reset()
    environment.short_action(JUMP)
    time.sleep(LONG)
    environment.short_actions([RIGHT, UP, DASH])
    environment.medium_action(JUMP)
    time.sleep(LONG)
    environment.medium_actions([RIGHT, UP, DASH])
    environment.reset()
