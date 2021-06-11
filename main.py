from celeste_environment import CelesteEnvironment
from simple_scorer import SimpleScorer
from blind_bot import BlindBot
from action import Action
from mask_search import MaskSearch
from moves import UP, LEFT, RIGHT, JUMP, DASH
import time
import random as rand


def move_gen(seed=None):
	ans = []
	rand.seed(seed)
	start_time = 0
	end_time = 50
	max_actions = 12
	moves = [UP, LEFT, RIGHT, JUMP, DASH]
	actions = rand.randint(0, max_actions) + 1
	for i in range(actions):
		move = rand.choice(moves)
		length = rand.randint(0, 20) + 1
		st = rand.randint(0, end_time - length)
		end = st + length
		ans.append(Action(st, move, 1))
		ans.append(Action(end, move, 0))
	ans = list(sorted(ans, key=lambda x: x.start_time))
	return ans

if __name__ == '__main__':
	env = CelesteEnvironment()
	searcher = MaskSearch()
	scorer = SimpleScorer(env, searcher)
	ideal_bot = [
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
	moves = move_gen()
	for i in range(len(moves)):
		print(moves[i])
	bot = BlindBot(env, moves)
	time.sleep(2)
	print(scorer.score(bot))
