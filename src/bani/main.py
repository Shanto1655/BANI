
"""Initial application entry point."""

from .conversation import get_conversation_response


def get_startup_message() -> str:
    """Return BANI's initial startup message."""
    return "Hello, buddy! I'm BANI. How can I help you?"


def main() -> None:
    """Run BANI's basic text conversation."""
    print(f"BANI: {get_startup_message()}")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBANI: Conversation ended.")
            break

        if message.strip().lower() in {"exit", "quit"}:
            print("BANI: Goodbye, buddy!")
            break

        response = get_conversation_response(message)
        print(f"BANI: {response}")


if __name__ == "__main__":
    main()
