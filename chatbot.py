
import json
import nltk
from nltk.stem import PorterStemmer
import re



stemmer = PorterStemmer()

with open("intents.json") as f:
    intents = json.load(f)

def preprocess(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return [stemmer.stem(word) for word in tokens]

def chatbot_response(user_input):
    user_words = preprocess(user_input)
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = preprocess(pattern)
            if any(word in user_words for word in pattern_words):
                return intent["responses"][0]
    return "Sorry, I did not understand that."

print("Chatbot is running (type 'quit' to exit)")
while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        break
    print("Bot:", chatbot_response(msg))
