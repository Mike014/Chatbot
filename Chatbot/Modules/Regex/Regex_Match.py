import re

class RegexMatch:
    def __init__(self, pattern):
        self.pattern = pattern 
        
    def match(self, text): # Returns a match object if the pattern is found in the text
        return re.match(self.pattern, text)

