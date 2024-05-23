import re
from Regex_Match import RegexMatch

class RegexSearch(RegexMatch):
    def search(self, text):
        return re.search(self.pattern, text)
    
    def findall(self, text):
        return re.findall(self.pattern, text)
    
