from src.langgraph_agenticai.state.state import State

class ChatbotWithWebsearchNode:
    """A chatbot node that integrates external web search capabilities."""

    def __init__(self, model):
        self.llm = model

    def process(self, state:State):

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])

        tools_response = f"Tool intgation response for input: {user_input}"

        return {"messages":[llm_response, tools_response]}
    
    def create_chatbot(self, tools):

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):

            return {"messages": llm_with_tools.invoke(state["messages"])}
        
        return chatbot_node