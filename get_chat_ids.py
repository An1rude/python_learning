from telethon import TelegramClient

api_id = 20621631  # Replace with your API ID
api_hash = 'c9a864b0b8399cf797b6ace98329d82c'  # Replace with your API hash

client = TelegramClient('get_chat_id_session', api_id, api_hash)

async def main():
    await client.start()
    print("✅ Logged in. Fetching chats...")

    async for dialog in client.iter_dialogs():
        print(f'📢 {dialog.name} - 🆔 {dialog.id}')

    await client.disconnect()

client.loop.run_until_complete(main())