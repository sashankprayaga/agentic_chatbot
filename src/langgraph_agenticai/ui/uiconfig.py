from configparser import ConfigParser
from pathlib import Path


class UIConfig:

    def __init__(self, config_file=None):
        if config_file is None:
            # Build a path to the config file relative to this file
            config_file = Path(__file__).parent / 'uiconfig.ini'
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config.get('DEFAULT', 'PAGE_TITLE', fallback='LangGraph AgenticAI')

    def get_page_icon(self):
        return self.config.get('DEFAULT', 'PAGE_ICON', fallback='📊')
    
    def get_llm_options(self):
        llm_options = self.config.get('DEFAULT', 'LLM_OPTIONS', fallback='Groq')
        return [option.strip() for option in llm_options.split(',')]
    
    def get_usecase_options(self):
        usecase_options = self.config.get('DEFAULT', 'USECASE_OPTIONS', fallback='Basic Chatbot, Chatbot with Tool, AI News, Blog Generator')
        return [option.strip() for option in usecase_options.split(',')]
    
    def get_groq_model_options(self):
        groq_model_options = self.config.get('DEFAULT', 'GROQ_MODEL_OPTIONS', fallback='mixral-8x7b, llama3-8b-8192, llama3-70b-8192, gemma2-9b-it')
        return [option.strip() for option in groq_model_options.split(',')]
    