import streamlit as st
import os
from src.langgraph_agenticai.ui.uiconfig import UIConfig


class LoadStreamlitUI:

    def __init__(self):
        self.ui_config = UIConfig()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.ui_config.get_page_title(), page_icon=self.ui_config.get_page_icon(), layout='wide')
        st.header(self.ui_config.get_page_title())


        with st.sidebar:

            # Get options from config
            llm_options = self.ui_config.get_llm_options()
            usecase_options = self.ui_config.get_usecase_options()

            # LLM Selection
            self.user_controls['llm'] = st.selectbox('Select LLM', llm_options)

            if self.user_controls['llm'] == 'Groq':

                # Groq Model Selection
                groq_model_options = self.ui_config.get_groq_model_options()
                self.user_controls['groq_model'] = st.selectbox('Select Groq Model', groq_model_options)
                self.user_controls['groq_api_key'] = st.text_input('Enter API Key', type='password', value=st.session_state.get('groq_api_key', ''))
                st.session_state['groq_api_key'] = self.user_controls['groq_api_key']
                

                # Validate Groq API Key
                if not self.user_controls['groq_api_key']:
                    st.warning('Please enter your Groq API Key to proceed.')

             # Use Case Selection
            self.user_controls['usecase'] = st.selectbox('Select Use Case', usecase_options)

            if self.user_controls['usecase'] == 'Chatbot with External Websearch':
                st.info('You have selected the Chatbot with External Websearch use case.')
                self.user_controls['tavily_api_key'] = st.text_input('Enter Tavily API Key', type='password', value=st.session_state.get('tavily_api_key', ''))
               

                if self.user_controls['tavily_api_key']:
                    os.environ['TAVILY_API_KEY'] = self.user_controls['tavily_api_key']
                    st.session_state['tavily_api_key'] = self.user_controls['tavily_api_key']

                if not self.user_controls['tavily_api_key']:
                    st.warning('Please enter your Tavily API Key to proceed.')

        return self.user_controls


