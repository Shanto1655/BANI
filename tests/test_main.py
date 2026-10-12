import unittest

from src.bani.main import get_startup_message


class TestStartupMessage(unittest.TestCase):
    def test_startup_message_is_a_string(self):
        message = get_startup_message()
        self.assertIsInstance(message, str)

    def test_startup_message_is_not_empty(self):
        message = get_startup_message()
        self.assertTrue(message.strip())


if __name__ == "__main__":
    unittest.main()
