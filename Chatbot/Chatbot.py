import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter

class My_chatbot:
    def __init__(self):
        pass
    def rule_based_chatbot(self):
        if "How are you" in input.lower():
            return "I'm good, how are you?"
        elif "What is your name" in input.lower():
            return "I'm Chatbot"
        else:
            return "I'm sorry, I don't understand"
        
    def retrieval_based_chatbot(self, input):
        responses = {
        "Hi": "Hello! How i can help you?",
        "Goodbye": "See you, was a pleasure for me help you"
    }
        if "Hi" in input.lower():
            return responses["Hi"]
        elif "Goodbye" in input.lower():
            return responses["Goodbye"]
        else:
            return "I'm sorry, I don't understand"
        
    def generative_chatbot(self, input):
        return "This would be your answer based on your question: " + input
    
    def preprocess_text(self, text):
        words = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        return filtered_words
    
    def n_grams(self, text, n=2):
        words = self.preprocess_text(text)
        n_grams = ngrams(words, n)
        return list(n_grams)
    
    def predict_next_words(self, text):
        corpus = "Natural language processing combines computer science, linguistics, and artificial intelligence to enable computers to process human languages. The goal is to enable computers to understand, interpret, and generate human languages in a valuable way. NLP is used to apply machine learning algorithms to text and speech."
        trigrams = self.generate_ngrams(corpus, 3)
        trigram_counts = Counter(trigrams)
        
        user_input_tokens = self.preprocess_text(text)
        last_two_words = tuple(user_input_tokens[-2:])
        
        suggestions = {trigram[-1]: count for trigram, count in trigram_counts.items() if trigram[:2] == last_two_words}
        
        if suggestions:
            return max(suggestions, key=suggestions.get)
        else:
            return "I'm sorry, I don't understand"
        
    def regex(self, input):
        patterns = {
            r'\bhi\b|\bhello\b': "Hello! How can I help you?",
            r'how\sare\syou': "I'm good, how are you?",
            r'what\s(is|\'s)\syour\sname': "I'm Chatbot",
            r'bgoodbye\b': "See you, was a pleasure for me help you",
            r'\bthanks\b|\bthank you\b': "You're welcome!",
            r'how\sdo\syou\swork': "I'm a chatbot, I can help you with your questions",
            r'what\s(is|\'s)\sNLP': "Natural language processing combines computer science, linguistics, and artificial intelligence to enable computers to process human languages. The goal is to enable computers to understand, interpret, and generate human languages in a valuable way. NLP is used to apply machine learning algorithms to text and speech.",
            r'can\syou\shelp\sm\swith\s[a-zA-Z]+': "I can help",
            }
        
        for pattern, response in patterns.items():
            if re.search(pattern, input.lower()):
                return response
            
            return "I'm sorry, I don't understand"
        

chatbot_test = My_chatbot()

print(chatbot_test.regex("Hi"))
        
        


    
    


        
            
       
        
        