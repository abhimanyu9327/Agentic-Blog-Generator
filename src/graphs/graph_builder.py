from langgraph.graph import StateGraph, START, END
from src.states.blogstate import BlogState

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
