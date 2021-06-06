from direct_keys import PressKey, ReleaseKey, W, A, S, D, ND1, ND2, ND3, Esc, Enter
import time


class CelesteEnvironment:
    """
    Class responsible for game environment and processing actions into the game.
    """
    def reset(self):
        """
        should restart current level in any case.
        """
        PressKey(Esc)
        time.sleep(0.2)
        ReleaseKey(Esc)
        PressKey(S)
        time.sleep(0.2)
        ReleaseKey(S)
        PressKey(Enter)
        time.sleep(0.2)
        ReleaseKey(Enter)
        time.sleep(4)

    def step(self, action):
        """
        should process AI actions into the game
        """
        pass

if __name__ == "__main__":
    time.sleep(3)
    CelesteEnvironment().reset()
