from src.states.blogstate import BlogState

class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            prompt = """Generate a title for the blog post on {topic}"""
            response = self.llm.invoke(prompt.format(topic=state["topic"]))
            return {"blog": {"title": response.content}}
