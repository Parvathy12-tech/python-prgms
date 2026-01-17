def feedback_system():
    try:
        name = input("Enter your name: ").strip()
        feedback = input("Enter your feedback: ").strip()

        if not name:
            raise ValueError("Error: Name cannot be empty.")
        if not feedback:
            raise ValueError("Error: Feedback cannot be empty.")

        print(f"Thank you, {name}! Your feedback: \"{feedback}\" has been recorded.")

    except ValueError as e:
        print(e)

    finally:
        print("Feedback session ended.")

feedback_system()