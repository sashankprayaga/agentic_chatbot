import os 
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:

    def __init__(self, user_controls_input):

        self.user_controls_input = user_controls_input


    def get_llm_model(self):

        try:    
            groq_api_key = self.user_controls_input["groq_api_key"]
            selected_groq_model = self.user_controls_input["groq_model"]
            if groq_api_key == "" or groq_api_key is None:
                st.error("Groq API Key is missing. Please enter your API key in the sidebar.")
            
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {e}")
        
        return llm