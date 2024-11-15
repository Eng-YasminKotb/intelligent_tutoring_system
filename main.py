from models.learner import Learner
from models.learning_object import LearningObject
from models.knowledge_graph import KnowledgeGraph
from recommender.recommender import Recommender

# Initialize learner
learner = Learner(
    learner_id=1,
    age=20,
    gender="male",
    basic_knowledge="beginner",
    learning_style={"preferred_formats": ["video", "text"]}
)

# Prompt learner to select a track
print("Choose a learning track: frontend, backend, mobile, basic")
selected_track = input("Enter your choice: ").strip().lower()

# Create and initialize knowledge graph dynamically
kg = KnowledgeGraph()
try:
    kg.initialize_graph_for_track(selected_track)
except ValueError as e:
    print(e)
    exit()

# Create learning objects (you can load these dynamically from a database or file)
lo_repository = [
    LearningObject("1", "HTML", "expository", 10, 1, "text"),
    LearningObject("2", "CSS", "expository", 15, 2, "video"),
    LearningObject("3", "JavaScript", "evaluative", 20, 3, "quiz"),
    LearningObject("4", "React", "expository", 25, 4, "video"),
    LearningObject("5", "Vue", "expository", 30, 4, "text")
]

# Recommender system
recommender = Recommender(learner, kg, lo_repository)

# Dynamic path recommendation based on track
start_topic = input("Enter the starting topic: ").strip()
end_topic = input("Enter the target topic: ").strip()

best_path = recommender.recommend_path(start_topic, end_topic)

print(f"Recommended Path for {selected_track.capitalize()} Development:", best_path)
