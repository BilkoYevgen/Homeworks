import unittest
from main import TelegramBot

class UnitTest(unittest.TestCase):
    def test_set_url(self):
        telegram_bot = TelegramBot("TG")
        telegram_bot.set_url("https://example.com")
        self.assertEqual(telegram_bot.url, "https://example.com")

    def test_set_chat_id(self):
        telegram_bot = TelegramBot("TG")
        telegram_bot.set_chat_id(12345)
        self.assertEqual(telegram_bot.chat_id, 12345)

if __name__ == '__main__':
    unittest.main()
