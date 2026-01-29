import os
from dotenv import load_dotenv

load_dotenv()

CITY = "tula"
CATEGORY = "kvartiry/prodam/1-komnatnye"
AVITO_URL = "https://www.avito.ru/tula/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?cd=1&f=ASgBAgECAkSSA8YQygiAWQFFxpoMHXsiZnJvbSI6MTAwMDAwMCwidG8iOjMwMDAwMDB9&localPriority=0"

MIN_PRICE = 1000000
MAX_PRICE = 4000000


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_ID")
