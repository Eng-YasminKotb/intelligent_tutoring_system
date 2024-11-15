class LearningObject:
    def __init__(self, lo_id, title, lo_type, duration, difficulty, format):
        self.lo_id = lo_id
        self.title = title
        self.lo_type = lo_type
        self.duration = duration
        self.difficulty = difficulty
        self.format = format
        self.ratings = []

    def update_difficulty(self, new_score, new_time):
        self.difficulty = 0.5 * self.difficulty + 0.3 * (1 - new_score / 10) + 0.2 * (new_time / self.duration)
