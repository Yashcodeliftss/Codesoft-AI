import re

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Simple predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm a chatbot, so I'm always good. How about you?"
    elif "what is your name" in user_input:
        return "I'm a simple rule-based chatbot."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Pattern matching for more complex queries
    elif re.search(r'\b(weather\b.*)', user_input):
        return "I'm not able to check the weather right now, but you can check it online."
    elif re.search(r'\btime\b', user_input):
        return "I don't have a watch, but you can check the time on your device."
    
    # Default response for unrecognized input
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Example interaction loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
