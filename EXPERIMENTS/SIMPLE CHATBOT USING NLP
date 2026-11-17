import random

responses = {
    "hello": ["Hello!", "Hi!", "How are you?"],
    "how are you": ["I am fine!", "Doing great!"],
    "bye": ["Goodbye!", "See you later!"]
}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    found = False

    for key in responses:
        if key in user:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand.")
