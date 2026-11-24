from collections import defaultdict, Counter

sequence = [
    "Start", "Login", "Browse", "Purchase",
    "Start", "Login", "Browse", "Logout",
    "Start", "Login", "Purchase"
]

transitions = defaultdict(Counter)

for i in range(len(sequence) - 1):
    current_event = sequence[i]
    next_event = sequence[i + 1]
    transitions[current_event][next_event] += 1

def predict_next(event):
    if event not in transitions:
        return "No prediction available"

    total = sum(transitions[event].values())

    probabilities = {
        next_event: count / total
        for next_event, count in transitions[event].items()
    }

    prediction = max(probabilities, key=probabilities.get)

    print("Current Event:", event)
    print("Transition Probabilities:", probabilities)
    print("Predicted Next Event:", prediction)

predict_next("Login")
