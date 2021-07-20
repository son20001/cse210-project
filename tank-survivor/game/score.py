class Score:
    def __init__(self, score = 0):
        self._score = score
    
    def display_text(self):
        return "Score: " + str(self._score)
    
    