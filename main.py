from celeste_environment import CelesteEnvironment
from simple_scorer import SimpleScorer
from blind_bot import BlindBot
from mask_search import MaskSearch
import time


if __name__ == '__main__':
	env = CelesteEnvironment()
	searcher = MaskSearch()
	scorer = SimpleScorer(env, searcher)
	bot = BlindBot(env, [])
	time.sleep(2)
	print(scorer.score(bot))