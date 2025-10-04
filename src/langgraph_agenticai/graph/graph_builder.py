from langgraph.graph import StateGraph , START, END
from src.langgraph_agenticai.state.state import State
from src.langgraph_agenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraph_agenticai.nodes.chatbot_with_wesbsearch import ChatbotWithWebsearchNode

class GraphBuilder:

    def __init__(self, model):
        
        self.llm = model
        self.graph_builder = StateGraph(State)

    
    def basic_chatbot_graph(self):

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def chatbot_with_websearch_graph(self):
        
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        ## Define ChatBot Node
        obj_chatbot_tool = ChatbotWithWebsearchNode(llm)
        chatbot_with_tools_node = obj_chatbot_tool.create_chatbot(tools)
        ##Add Nodes
        self.graph_builder.add_node("chatbot", chatbot_with_tools_node)
        self.graph_builder.add_node("tools",tool_node)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot", END)





    def setup_graph(self, usecase):

        if usecase == "Basic Chatbot":
            self.basic_chatbot_graph()
           
        elif usecase == "Chatbot with External Websearch":
            self.chatbot_with_websearch_graph()
            
        
        else:
            raise ValueError(f"Unsupported use case: {usecase}")
        
        return self.graph_builder.compile()