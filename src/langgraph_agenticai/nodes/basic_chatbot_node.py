
from src.langgraph_agenticai.state.state import State



class BasicChatbotNode:
    """A basic chatbot node for handling user interactions."""

    def __init__(self, model):
        self.llm = model

    
    def process(self, state:State):
        """Process the user input and generate a response."""

        return {"messages":self.llm.invoke(state["messages"])}