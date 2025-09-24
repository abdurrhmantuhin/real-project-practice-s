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


def demonstrate_slicing(self,text):
    print(f"\n starting slicing demonstrate")
    print(f"original text: '{text}'")
    print(f"length: {len(text)} charecters!")

    print(f"\n first 5 charecters: '{text[:5]}'")
    print(f"last 5 charecters: '{text[-5:]}'")
    print(f"midle charecters: '{text[5:15]}'")
    print(f"everyothers charecters: {text[::2]}")
    print(f"revers the string: {text[::-1]}")

    if len(text) > 10 :
        first_space = text.find(' ')
        if first_space != -1 :
            first_word = text[:first_space]
            print(f"first word: {first_word}")

        if '.' in text:
            extension = text[text.rfind('.'):]
            print(f"file extension: '{extension}'")
    print(F"\nnagative indexing exmple:")
    print(F"last charecter: {text[-1]}")
    print(F"second two latter: {text[-2]}")
    print(F"last 3 charecters: {text[-3]}")
    return text