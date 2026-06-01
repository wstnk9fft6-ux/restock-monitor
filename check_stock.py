import requests

URL = "https://thebeardeddragongames.crystalcommerce.com/catalog/one_piece_op16_the_time_of_battle/14954?filter_by_stock=out-of-stock"

DISCORD_WEBHOOK = "YOUR_WEBHOOK_HERE"

def send_alert(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

def check_stock():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers)
    text = r.text.lower()

    if "add to cart" in text or "in stock" in text:
        send_alert("🚨 OP-16 MAY BE IN STOCK RIGHT NOW!")
    else:
        print("Still out of stock")

check_stock()