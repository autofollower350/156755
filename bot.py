from pyrogram import Client, filters

app = Client("m3u8_video_bot", api_id=12345, api_hash="your_api_hash", bot_token="your_bot_token")

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Send me a .txt file containing M3U8 video links, and I'll download and upload them!")

app.run()
