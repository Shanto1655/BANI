
import unittest

from src.bani.main import get_startup_message
from src.bani.commands import get_response, handle_command
from src.bani.conversation import get_conversation_response

from src.bani.input_validation import (
    MAX_MESSAGE_LENGTH,
    normalize_message,
    validate_message,
)


class TestStartupMessage(unittest.TestCase):
    def test_startup_message_is_a_string(self):
        self.assertIsInstance(get_startup_message(), str)

    def test_startup_message_is_not_empty(self):
        self.assertTrue(get_startup_message().strip())


class TestResponse(unittest.TestCase):
    def test_response_includes_user_message(self):
        self.assertEqual(
            get_response("Hello BANI"),
            "I heard you say: Hello BANI",
        )

    def test_response_trims_extra_spaces(self):
        self.assertEqual(
            get_response("  Hello BANI  "),
            "I heard you say: Hello BANI",
        )

    def test_empty_message_gets_helpful_response(self):
        self.assertEqual(
            get_response("   "),
            "You haven't typed anything yet.",
        )


class TestCommandHandler(unittest.TestCase):
    def test_help_command(self):
        self.assertIn("Available commands", handle_command("help"))

    def test_version_command(self):
        self.assertEqual(handle_command("version"), "BANI version 0.1.0")

    def test_greeting_command(self):
        self.assertIn("Hello", handle_command("hi"))

    def test_commands_ignore_case_and_outer_spaces(self):
        self.assertEqual(handle_command("  HELP  "), handle_command("help"))

    def test_unknown_message_returns_none(self):
        self.assertIsNone(handle_command("Explain quantum computing"))


class TestConversationManager(unittest.TestCase):
    def test_recognized_command_uses_command_response(self):
        self.assertIn(
            "Available commands",
            get_conversation_response("help"),
        )

    def test_unknown_message_uses_fallback(self):
        self.assertEqual(
            get_conversation_response("Explain quantum computing"),
            "I heard you say: Explain quantum computing",
        )

    def test_empty_message_is_handled(self):
        self.assertEqual(
            get_conversation_response("   "),
            "You haven't typed anything yet.",
        )


class TestInputValidation(unittest.TestCase):
    def test_normalize_removes_outer_spaces(self):
        self.assertEqual(normalize_message("  hello  "), "hello")

    def test_valid_message_has_no_validation_error(self):
        self.assertIsNone(validate_message("hello"))

    def test_empty_message_is_rejected(self):
        self.assertIsNotNone(validate_message(""))

    def test_message_at_limit_is_allowed(self):
        message = "a" * MAX_MESSAGE_LENGTH
        self.assertIsNone(validate_message(message))

    def test_message_over_limit_is_rejected(self):
        message = "a" * (MAX_MESSAGE_LENGTH + 1)
        self.assertIsNotNone(validate_message(message))

    def test_conversation_handles_whitespace_only_input(self):
        self.assertEqual(
            get_conversation_response("   "),
            "You haven't typed anything yet.",
        )


if __name__ == "__main__":
    unittest.main()
