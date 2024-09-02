print("hi")
import time

time.sleep(5.0)  # Sleep for 1.0 seconds

print("whats up")
import time

time.sleep(5.0)  # Sleep for 1.0 seconds

print("i am tacOS v1.0 for ios and android made by Luka") # will update
import time

time.sleep(5.0)  # Sleep for 1.0 seconds
print("credits to Matthew , Hamish + Oliver + Alex ") #they are my friends
import time

time.sleep(10.0)  # Sleep for 1.0 seconds
# Define a dictionary with some predefined responses
responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
    "yes" : "ok",
    "erm actually thats wrong" : "NERD ALERT NERD ALERT NERD ALERT",
    "tounge twister" : "i found some mud and i put it in a mug",
    "what raspberry pis can this run on" : "Almost Any Pi just needs thonny",
    "can this run on windows or mac" : "not recommended but as long as you have thonny installed yes",
    "can we mod the code" : "yeah sure just dont do anything illegal or do anything deemed ma 15 for aus adults only for us and 18 for eur",
    "can you speak chinese" : "ni hao that means hello",
    "no" : "aw dang it",
    "WELCOME TO THE GULAG" : "pls help",
}









def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    # Check if the user input matches any predefined questions
    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I don't understand that."

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
