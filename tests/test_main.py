
import unittest

from src.bani.main import get_response, get_startup_message


class TestStartupMessage(unittest.TestCase):
    def test_startup_message_is_a_string(self):
        message = get_startup_message()
        self.assertIsInstance(message, str)

    def test_startup_message_is_not_empty(self):
        message = get_startup_message()
        self.assertTrue(message.strip())


class TestResponse(unittest.TestCase):
    def test_response_includes_user_message(self):
        response = get_response("Hello BANI")
        self.assertEqual(response, "I heard you say: Hello BANI")

    def test_response_trims_extra_spaces(self):
        response = get_response("  Hello BANI  ")
        self.assertEqual(response, "I heard you say: Hello BANI")

    def test_empty_message_gets_helpful_response(self):
        response = get_response("   ")
        self.assertEqual(response, "You haven't typed anything yet.")


if __name__ == "__main__":
    unittest.main()
