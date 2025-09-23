import re 
import os
import json
from datetime import datetime

class TextAnalyzer:
    def __init__(self):
        print("="* 60)
        print("welcome to the text analyzer!")
        print("="* 60)
        
        self.app_name = 'text analyzier pro'
        self.welcome_massage = "welcome to john's text analysis tool!!!"

        self.help_text = """
        this tool can help you:
        - analyze text files
        - count words and charecters 
        - clean and formate text
        - extract important information
        """

        self.default_path = r"C:\Users\GOAT TUHIN\Documents\books\The Lean Startup - Erick Ries"
        self.current_text = ""
        self.separator = "\n" + "="*50 + "\n"

        print(f"App name: {self.app_name}")
        print(F"massage: {self.welcome_massage}")
        print(f"help: {self.help_text}")