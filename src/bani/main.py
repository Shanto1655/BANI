"""Initial application entry point."""


def get_startup_message() -> str:
    """Return BANI's initial startup message."""
    return "BANI is starting. Core systems are not implemented yet."


def main() -> None:
    """Start the BANI application."""
    print(get_startup_message())


if __name__ == "__main__":
    main()
