import time


class SimpleScorer:
    """
    Class responsible for scoring bot actions.
    """
    def __init__(self, environment, searcher):
        self.environment = environment
        self.searcher = searcher

    def score(self, bot):
        result = -1
        self.environment.reset()
        bot.do()
        #Pause before finding MH for stabilasing bot position.
        time.sleep(5)
        center = self.searcher.search_MH()
        #print('MH Position:', center)
        center_x = center[0]
        if center_x <= 125:
            result = 0
        elif 235 <= center_x <= 315:
            result = 1
        elif 425 <= center_x <= 535:
            result = 2
        elif 725 <= center_x:
            result = 3
        return result
