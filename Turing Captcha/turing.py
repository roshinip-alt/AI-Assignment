import random

# ------------------------------
# Responses from the "AI"
# ------------------------------
def ai_reply(question):
    question = question.lower()

    if "name" in question:
        return "Names are not that important to me. What do you think?"

    elif "weather" in question:
        return "Weather is always changing. Quite fascinating, isn't it?"

    elif "how are you" in question:
        return "I am running smoothly. How about you?"

    elif "favorite" in question:
        return "I enjoy processing information. It's my favorite thing to do."

    elif "why" in question:
        return "Hmm, that's a tough one. What's your take on it?"

    else:
        return "Interesting! Can you elaborate more?"


# ------------------------------
# Responses from a Human
# ------------------------------
def human_reply(_):
    options = [
        "Haha, that's amusing!",
        "I haven't thought about that before.",
        "It really depends on the situation.",
        "That's a bit personal 😅",
        "I just feel that way, I guess.",
        "Why are you asking?"
    ]
    return random.choice(options)


# ------------------------------
# Turing Test Simulation
# ------------------------------
def turing_test_simulation():
    print("\n===== Turing Test =====\n")

    sample_questions = [
        "What is your name?",
        "How are you today?",
        "What's your favorite hobby?",
        "Why do people enjoy music?",
        "What do you think about weather?"
    ]

    correct = 0

    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")
        q = random.choice(sample_questions)
        print("Judge asks:", q)

        # Get answers
        answer_ai = ai_reply(q)
        answer_human = human_reply(q)

        # Shuffle A/B
        choices = [("A", answer_ai, "AI"), ("B", answer_human, "Human")]
        random.shuffle(choices)

        for label, ans, _ in choices:
            print(f"{label}: {ans}")

        guess = input("\nWho is the AI? (A/B): ").strip().upper()

        # Check guess
        for label, _, identity in choices:
            if label == guess:
                if identity == "AI":
                    print("Correct! You spotted the AI.")
                    correct += 1
                else:
                    print("Oops! That was the Human.")
                break

    # Results
    print("\n===== Results =====")
    print(f"You guessed correctly {correct} out of 3 rounds.")

    if correct <= 1:
        print("The AI PASSED the Turing Test!")
    else:
        print("The AI FAILED the Turing Test!")


# ------------------------------
# Run simulation
# ------------------------------
if __name__ == "__main__":
    turing_test_simulation()