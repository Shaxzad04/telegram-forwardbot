from telethon import TelegramClient, events

# Bu yerga my.telegram.org dan olingan ma'lumotlarni yozasiz
api_id = chat id          # <- bu yerga sizning api_id
api_hash = 'bot token' # <- bu yerga sizning api_hash
source_channel = 'https://t.me/kunuz'  # manba kanal @sizni_qiziqtirgan_kanal
target_channel = 'https://t.me/UzTechWorlds'    # sizning kanal

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
client.run_until_disconnected()
