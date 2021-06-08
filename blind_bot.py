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
        for action in actions:
            pass