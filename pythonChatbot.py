import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.data import find
from rich.console import Console

"""
#it is given as command line, because it downloads the package for every time, if you want to download the remove the triple quote at the strat and end
# Function to check if a package is already downloaded
def download_nltk_package(package):
    try:
        find(package)
    except LookupError:
        nltk.download(package)

# Download only if not already installed
download_nltk_package('punkt')
download_nltk_package('averaged_perceptron_tagger')
download_nltk_package('stopwords')
download_nltk_package('wordnet')
"""

# Predefined responses for basic queries
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "thanks": ["You're welcome!", "Anytime! Happy to help!"],
    "weather" : ["Click the link to know the weather:\n [bold blue link=https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN1055IN1055&oq=weather&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhGGIACGIAEMgcIARAAGIAEMgoIAhAAGMkDGIAEMg0IAxAAGJIDGIAEGIoFMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgoICBAuGNQCGIAEMgcICRAAGI8C0gEINDQ1M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8]Click Here[/]"],
    "chatbot": ["Here is the link were you can find my upgraded versions—you can use them to improve your experience even further:\n [bold blue link=https://www.google.com/search?q=list+all+the+available+chatbots&sca_esv=1e4d509914ca8c34&rlz=1C1CHBF_enIN1055IN1055&sxsrf=AHTn8zqVAhyCniCPueHrBKJD8OwqicbyIg%3A1738984883037&ei=s82mZ5X9AdOE4-EPpNLZwA8&ved=0ahUKEwjVouTBj7OLAxVTwjgGHSRpFvgQ4dUDCBA&uact=5&oq=list+all+the+available+chatbots&gs_lp=Egxnd3Mtd2l6LXNlcnAiH2xpc3QgYWxsIHRoZSBhdmFpbGFibGUgY2hhdGJvdHMyBRAhGKABMgUQIRigATIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FMgUQIRifBTIFECEYnwUyBRAhGJ8FSIdPUABYj01wAHgBkAEAmAGFAqAB2SOqAQYwLjMwLjG4AQPIAQD4AQGYAh-gAr8kwgIKECMYgAQYJxiKBcICBBAjGCfCAhAQLhiABBjRAxjHARgnGIoFwgILEC4YgAQY0QMYxwHCAgUQLhiABMICBRAAGIAEwgIKEAAYgAQYQxiKBcICChAuGIAEGEMYigXCAgYQABgWGB7CAgYQABgNGB7CAgcQIRigARgKmAMAkgcGMC4zMC4xoAeK-QE&sclient=gws-wiz-serp]Click Here[/]"],
    "cricbuzz": ["Click the link to know the scores:\n [bold blue link=https://www.cricbuzz.com/]Click Here[/]"],
    "onefootball": ["Click the link to know the scores:\n [bold blue link=https://onefootball.com/en/home]Click Here[/]"],
    "capabilities": ["I can show you weather,\n I can give you the ideas for your projects, assignments, tasks\n I can show you scores of football and cricket"],
    "default": ["I'm not sure I understand. Could you rephrase that?", "Can you clarify your question?"]
}

# Intent detection function
def get_intent(text):
    tokens = word_tokenize(text.lower())
    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye"]):
        return "goodbye"
    elif any(word in tokens for word in ["thank", "thanks"]):
        return "thanks"
    elif any(word in tokens for word in ["weather", "climate"]):
        return "weather"
    elif any(word in tokens for word in ["queries", "project","assignment","task","chatbot"]):
        return "chatbot"
    elif any(word in tokens for word in ["cricket"]):
        return "cricbuzz"
    elif any(word in tokens for word in ["football"]):
        return "onefootball"
    elif any(word in tokens for word in ["capabilities", "assist"]):
        return "capabilities"
    return "default"

# Chatbot response function
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Main chat loop
def chat():
    print("Chatbot: Hello! Type 'exit' to end the chat.\nIf generates link you can press 'ctrl+left_click' the link to view the link")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        console = Console()
        console.print(f'Chatbot: {response}')

if __name__ == "__main__":
    chat()
