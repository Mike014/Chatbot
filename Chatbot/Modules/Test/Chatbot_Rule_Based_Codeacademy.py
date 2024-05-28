import re
import unittest
from urllib import response

class SupportBot:
    def __init__(self):
        self.intents = {
            'how_to_pay_bill': [r'.*how.*pay bills.*', r'.*how.*pay my bill.*'],
            'pay_bill': [r'.*want.*pay my bill.*', r'.*need./pay my bill.+']
            }
        
    def how_to_pay_bill_intent(self):
        return "You can pay your bill a variety of ways. You can pay online or via phone at 555-1234."
    
    def pay_bill_intent(self):
        return "You can pay your bill a variety of ways. You can pay online or via phone at 555-1234."
    
    def match_reply(self, reply):
        for intent, patterns in self.intents.items():
            for pattern in patterns:
                if re.match(pattern, reply):
                    if intent == 'how_to_pay_bill':
                        return self.how_to_pay_bill_intent()
                    elif intent == 'pay_bill':
                        return self.pay_bill_intent()
        raise ValueError("I'm sorry, I'm not sure how to help you.")
    
    def handle_conservation(self):
        try: 
            while True:
                user_input = input("User: ")
                if not isinstance(user_input, str):
                    raise TypeError("Please enter a valid string.")
                response = self.match_reply(user_input)
                print(response)
                if user_input == 'quit':
                    break
        except ValueError as e:
            print(f"ValueError: {e}")

# Test
if __name__ == '__main__':
    bot = SupportBot()
    bot.handle_conservation()            



        

            
            
            
            
                
            


            
            



    
        





                
                
                
                
            
        
            
            
        
            
        
            
            
        
            
            

        




