import json
import nltk

class Tokenizer:
    def __init__(self,jsonPath) -> None:
        '''
        Initialize the Tokenizer constructor
        Input: FilePath to settings.json
        '''
        try:
            self.data=json.load(jsonPath)
            print("Installing all necessary files please wait")
            nltk.download("all")
        except Exception as E:
            print(E)

