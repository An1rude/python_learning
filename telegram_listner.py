from telethon import TelegramClient, events
import re

# ======= REPLACE WITH YOUR OWN CREDENTIALS =======
api_id = 20621631  # ← Replace with your real API ID
api_hash = 'c9a864b0b8399cf797b6ace98329d82c'  # ← Replace with your real API hash

# ======= The Telegram channel or group username =======
# Use '@channelname' or just 'channelname'
# If it's a private group, you'll need the chat ID
signal_source = -1002163454656  # ← Replace with the real name

# ======= Setup Telegram client =======
client = TelegramClient('bot_session', api_id, api_hash)

# ======= Signal parser function =======
def parse_signal(message):
    pattern = r'(BUY|SELL)\s+([A-Z]+\/?[A-Z]*)\s*@?\s*([\d.]+)?'
    match = re.search(pattern, message, re.IGNORECASE)
    if match:
        action = match.group(1).upper()
        pair = match.group(2).replace("/", "").upper()
        price = match.group(3) or "market"
        return {"action": action, "pair": pair, "price": price}
    return None

# ======= Telegram message handler =======
@client.on(events.NewMessage(chats=signal_source))
async def handler(event):
    msg = event.message.message
    print("Received:", msg)

    signal = parse_signal(msg)
    if signal:
        print("✅ Parsed Signal:", signal)
        # 🔜 Here we will send the order to Mudrex
    else:
        print("❌ No valid signal found.")

# ======= Start the bot =======
client.start()
print("🚀 Listening for signals...")
client.run_until_disconnected()
