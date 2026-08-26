from src.states.blogstate import BlogState

class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            prompt = """
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                   """
            sytem_message = prompt.format(topic=state["topic"])
            print(sytem_message)
            response = self.llm.invoke(sytem_message)
            print(response)
            return {"blog": {"title": response.content}}
