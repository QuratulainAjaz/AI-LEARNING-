print("Welcome to Fake ChatGPT! Type 'exit' to quit.\n")

# Loop for interactive conversation
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    # Temperature experiment (simulate creativity)
    temperatures = [0.1, 0.5, 1.0]  # Low, medium, high creativity
    fake_responses = {
        0.1: "Hello. I am fine. How can I assist you?",
        0.5: "Hi there! I’m doing well. How about you today?",
        1.0: "Hey! I’m great, feeling awesome! What’s up with you?"
    }

    print("=== AI Replies by Temperature ===")
    for temp in temperatures:
        print(f"Temperature {temp}: {fake_responses[temp]}")
    print()  # blank line

    # Optional: text file summarization demo
    try:
        with open("sample.txt", "r") as file:
            text = file.read()

        print("=== Original Text ===")
        print(text, "\n")

        summary = "AI is a branch of computer science that creates machines capable of human-like tasks, used in various fields."
        print("=== AI Summary ===")
        print(summary)
        print("\n---\n")  # separate different rounds nicely

    except FileNotFoundError:
        print("No sample.txt file found. Skipping summarization.\n---\n")