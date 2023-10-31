class Action:
    def __init__(self, start_time, move, hold):
        self.start_time = start_time
        self.move = move
        self.hold = hold


    def __str__(self):
    	return f"Action(start_time={self.start_time}, move={self.move}, hold={self.hold})"
    	