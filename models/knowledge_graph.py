import networkx as nx


class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_topic(self, topic_id, dependencies=None):
        self.graph.add_node(topic_id)
        if dependencies:
            for dep in dependencies:
                self.graph.add_edge(dep, topic_id)

    def get_paths(self, start_topic, end_topic):
        return list(nx.all_simple_paths(self.graph, source=start_topic, target=end_topic))

    def initialize_graph_for_track(self, track):
        if track == "frontend":
            self.add_topic("HTML")
            self.add_topic("CSS", dependencies=["HTML"])
            self.add_topic("JavaScript", dependencies=["CSS"])
            self.add_topic("React", dependencies=["JavaScript"])
            self.add_topic("Vue", dependencies=["JavaScript"])

        elif track == "backend":
            self.add_topic("Basics of Programming")
            self.add_topic("Databases", dependencies=["Basics of Programming"])
            self.add_topic("Node.js", dependencies=["Databases"])
            self.add_topic("Express", dependencies=["Node.js"])
            self.add_topic("Authentication", dependencies=["Express"])

        elif track == "mobile":
            self.add_topic("Basics of Programming")
            self.add_topic("Mobile UI", dependencies=["Basics of Programming"])
            self.add_topic("Flutter", dependencies=["Mobile UI"])
            self.add_topic("React Native", dependencies=["Mobile UI"])

        elif track == "basic":
            self.add_topic("Variables")
            self.add_topic("Loops", dependencies=["Variables"])
            self.add_topic("Functions", dependencies=["Loops"])
            self.add_topic("Data Structures", dependencies=["Functions"])
        else:
            raise ValueError(f"Track '{track}' is not supported.")
