from services.openai_service import chat_completion


def main():
    print("ChatCompletion app started.")
    print("Type 'exit' to end conversation.")

    conversation_history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        conversation_history.append(f"You: {user_input}")
        model_response = chat_completion("\n".join(conversation_history))

        print(f"Model: {model_response}")
        conversation_history.append(f"Model: {model_response}")


if __name__ == "__main__":
    main()
