class Learner:
    def __init__(self, learner_id, age, gender, basic_knowledge, learning_style):
        self.learner_id = learner_id
        self.age = age
        self.gender = gender
        self.basic_knowledge = basic_knowledge
        self.learning_style = learning_style  # e.g., {"preferred_formats": ["video", "text"]}
        self.learning_log = []
        self.current_ability = 0.0

    def log_interaction(self, lo_id, score, time_spent, attempts):
        interaction = {"lo_id": lo_id, "score": score, "time_spent": time_spent, "attempts": attempts}
        self.learning_log.append(interaction)

    def calculate_ability(self):
        if not self.learning_log:
            return
        total_score = sum(log['score'] for log in self.learning_log)
        total_time = sum(log['time_spent'] for log in self.learning_log)
        total_attempts = sum(log['attempts'] for log in self.learning_log)
        num_logs = len(self.learning_log)
        self.current_ability = (0.4 * (total_score / num_logs) -
                                0.3 * (total_time / num_logs) -
                                0.3 * (total_attempts / num_logs))
