import streamlit as st
from src.langgraph_agenticai.ui.streamlit.loadui import LoadStreamlitUI
from src.langgraph_agenticai.LLM.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlit.display_resultui import DisplayResultUI


def load_langrapg_agenticai_app():

    """Load the LangGraph AgenticAI Streamlit application."""
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("User input is required to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here...")

    if user_message:

        try:
            ## Configure the llm
            obj_llm  = GroqLLM(user_controls_input=user_input)
            model = obj_llm.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model. Please check your configuration.")
                return
            
            # Initialize and run the app based on the selected use case
            usecase = user_input.get('usecase')

            if not usecase:
                st.error("Use case is required to proceed.")
                return
            
            ## Graph Builder
            graph_builder = GraphBuilder(model=model)

            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                DisplayResultUI(usecase=usecase, graph=graph, user_message=user_message).display_result()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return
        
        except Exception as e:
            st.error(f"Error: LLM configuration failed - {e}")
            return


                