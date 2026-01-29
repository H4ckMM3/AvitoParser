import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_message(text):
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    
    response = requests.post(TELEGRAM_API_URL, data=data)
    try:
        return response.ok
    except Exception as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")
        return False