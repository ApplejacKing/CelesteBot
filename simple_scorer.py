import time


#Borders for evaluator: <120; 240-310; 430-530; 740>

class SimpleScorer:
    """
    Class responsible for scoring bot actions.
    """
    def __init__(self, environment):
        self.environment = environment

    def score(self, bot):
        result = 0
        self.environment.reset()
        bot.do()
        #Pause before finding MH for stabilasing bot position.
        time.sleep(3)
        #TODO: MH search
        #TODO: Evaluating depending on MH position
        return result