
import unittest

from src.bani.main import (
    get_response,
    get_startup_message,
    handle_command,
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


if __name__ == "__main__":
    unittest.main()
