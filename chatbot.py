print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")
    elif user == "how are you":
        print("Bot: I'm doing great!")
    elif user == "your name":
        print("Bot: I'm a simple AI chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that yet.")
