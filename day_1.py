print("🤖 Hello! I'm ChatBot. Let's chat!")

# Asking for the user's name
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

# Chat loop
while True:
    user_input = input("> ").lower()  # convert to lowercase for easier comparison

    # Exit condition
    if user_input == "bye":
        print("Goodbye! Have a great day! 👋")
        break

    # Greeting responses
    elif user_input in ["hi", "hello", "hey"]:
        print("Hello there!")

    # Responding to "how are you?"
    elif "how are you" in user_input:
        print("I'm just a bunch of code, but I'm doing great! 😊 What about you?")

    # Responding to feelings
    elif "sad" in user_input:
        print("I'm sorry to hear that. I'm here if you want to talk. 💙")

    elif "happy" in user_input:
        print("Yay! I'm glad to hear that! 🎉")

    # Default response
    else:
        print("Hmm... I don't understand that, but I'm learning!")

