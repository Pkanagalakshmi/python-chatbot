import re
import random
from datetime import datetime

class Chatbot:
    def __init__(self):
        self.patterns = {
            r'hi|hello|hey': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Nice to meet you!"
            ],
            r'how are you': [
                "I'm doing great, thanks for asking!",
                "I'm fine, thank you! How are you?",
                "I'm excellent! How about you?"
            ],
            r'what time': [
                f"It's currently {datetime.now().strftime('%I:%M %p')}",
                f"The time is {datetime.now().strftime('%I:%M %p')}"
            ],
            r'what date': [
                f"Today is {datetime.now().strftime('%B %d, %Y')}",
                f"It's {datetime.now().strftime('%B %d, %Y')}"
            ],
            r'bye|goodbye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            r'help': [
                "I can help you with:\n- Greetings\n- Time and date\n- Basic conversation\nJust ask me anything!",
                "Here's what I can do:\n- Respond to greetings\n- Tell you the time and date\n- Chat with you\nWhat would you like to know?"
            ]
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return "I'm not sure I understand. Could you rephrase that or ask for 'help' to see what I can do?"

def main():
    chatbot = Chatbot()
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    print("Chatbot: How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()