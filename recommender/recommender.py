import math

class Recommender:
    def __init__(self, learner, knowledge_graph, lo_repository):
        self.learner = learner
        self.kg = knowledge_graph
        self.lo_repo = lo_repository

    def recommend_path(self, start_topic, end_topic):
        paths = self.kg.get_paths(start_topic, end_topic)
        best_path = None
        best_score = -math.inf

        for path in paths:
            total_score = 0
            for topic in path:
                lo = self.select_lo_for_topic(topic)
                total_score += self.evaluate_lo_fit(lo)

            if total_score > best_score:
                best_path = path
                best_score = total_score

        return best_path

    def select_lo_for_topic(self, topic):
        candidate_los = [lo for lo in self.lo_repo if lo.title == topic]
        best_lo = max(candidate_los, key=lambda lo: self.evaluate_lo_fit(lo))
        return best_lo

    def evaluate_lo_fit(self, lo):
        fit_score = 0
        if lo.format in self.learner.learning_style["preferred_formats"]:
            fit_score += 1
        fit_score -= abs(lo.difficulty - self.learner.current_ability)
        return fit_score
