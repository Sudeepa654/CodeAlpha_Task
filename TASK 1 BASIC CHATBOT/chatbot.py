
def greet_user():
    print("Welcome to SimpleChatBot!")
    print("You can type 'hello', 'how are you', or 'bye'.")
    print("Type your message below to start chatting...\n")

def get_bot_response(user_input):
    user_input = user_input.strip().lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "":
        return "You didn't type anything!"
    else:
        return "I'm not sure how to respond to that."

def run_chatbot():
    greet_user()

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)

        if user_input.strip().lower() == "bye":
            break

    print("\nChat ended. Have a great day!")

if __name__ == "__main__":
    run_chatbot()
