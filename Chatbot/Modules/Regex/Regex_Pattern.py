import re
from Regex.Regex_Search import RegexSearch 
from Regex_Match import RegexMatch

WORD = re.compile(r'\w+') # Matches any word character (alphanumeric & underscore)
NON_WORD = re.compile(r'\W+') # Matches any non-word character
DIGITS = re.compile(r'\d+') # Matches any digit
NON_DIGITS = re.compile(r'\D+') # Matches any non-digit
WHITESPACE = re.compile(r'\s+') # Matches any whitespace character
NON_WHITESPACE = re.compile(r'\S+') # Matches any non-whitespace character
WORD_BOUNDARY = re.compile(r'\b') # Matches a word boundary

# The following functions return a compiled regular expression pattern
def word_starting_with(prefix):
    return re.compile(r'\b' + re.escape(prefix) + r'\w*\b')

def word_ending_with(suffix):
    return re.compile(r'\b\w*' + re.escape(suffix) + r'\b')

def word_containing(substring):
    return re.compile(r'\b\w*' + re.escape(substring) + r'\w*\b')

def word_followed_by(word, following):
    return re.compile(r'\b' + re.escape(word) + r'\b(?=' + re.escape(following) + r')')

def word_preceded_by(word, preceding):
    return re.compile(r'(?<=' + re.escape(preceding) + r')\b' + re.escape(word) + r'\b')

def case_sensitive(pattern):
    return re.compile(pattern, re.IGNORECASE)

def compile_and_search(pattern):
    compile_pattern = re.compile(pattern)
    return RegexSearch(compile_pattern)

# # Test RegexMatch class with the following code
# if __name__ == '__main__':
#     text = 'Hello, World!'
#     pattern = [WORD, NON_WORD, DIGITS, NON_DIGITS, WHITESPACE, NON_WHITESPACE, WORD_BOUNDARY]
    
#     for p in pattern:
#         regex = RegexMatch(p)
#         match = regex.match(text)
#         if match:
#             print(f'{p.pattern} found in text: {match.group()}')
#         else:
#             print(f'{p.pattern} not found in text')
    

        


 
