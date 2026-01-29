import json
import os
from parser import get_listings
from telegram_bot import send_message

DATA_FILE = "data.json"

def load_old_data():
    if not os.path.exists(DATA_FILE):
        return set()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        if not content:
            return set()
        data = json.loads(content)
        return set(data)
    
def save_links(links):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(list(links), f, ensure_ascii=False, indent=2)
        
def init_read():
    listings = get_listings()
    links = {normalize_link(item['link']) for item in listings if item.get('link')}
    save_links(links)
    print(f"Сохранено {len(links)} объявлений. Теперь уведомления будут только о новых.")


def normalize_link(link):
    return link.split('?')[0] if link else link

def send_notification(item):
    message = f"🔔 Объявление уже существует: {item['title']}\n💰 Цена: {item['price']}\n🔗 {item['link']}"
    send_message(message)
        
def main():
    old_links = load_old_data()
    new_links = set()
    listings = get_listings()
    for item in listings:
        if normalize_link(item['link']) not in old_links:
            message = f"🔔 Объявление уже существует: {item['title']}\n💰 Цена: {item['price']}\n🔗 {item['link']}"
            send_message(message)
            new_links.add(normalize_link(item['link']))
    all_links = old_links.union(new_links)
    save_links(all_links)
    print(f"Найдено {len(new_links)} новых объявлений")
        
if __name__ == "__main__":
    main()