from celeste_environment import CelesteEnvironment
from simple_scorer import SimpleScorer
from blind_bot import BlindBot
from action import Action
from mask_search import MaskSearch
from moves import UP, LEFT, RIGHT, JUMP, DASH, move2key
import time


if __name__ == '__main__':
	env = CelesteEnvironment()
	searcher = MaskSearch()
	scorer = SimpleScorer(env, searcher)
	moves = [
		Action(1, JUMP, 1),
		Action(3, DASH, 1),
		Action(4, JUMP, 0),
		Action(4, DASH, 0),
		Action(8, UP, 1),
		Action(8, RIGHT, 1),
		Action(9, JUMP, 1),
		Action(11, DASH, 1),
		Action(11, JUMP, 0),
		Action(12, DASH, 0),
		Action(17, JUMP, 1),
		Action(18, DASH, 1),
		Action(19, DASH, 0),
		Action(19, JUMP, 0),	
		Action(25, UP, 0),
		Action(25, RIGHT, 0),
	]
	bot = BlindBot(env, moves)
	time.sleep(2)
	print(scorer.score(bot))