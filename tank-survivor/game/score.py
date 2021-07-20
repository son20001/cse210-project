class Score:
    def __init__(self, score = 0):
        self._score = score
    
    def display_text(self):
        return "Score: " + str(round(self._score,1))
    
    def get_score(self):
        return self._score

    def add_score(self, score = 0.1):
        self._score += score
    