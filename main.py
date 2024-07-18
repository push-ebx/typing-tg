from env import API_ID, API_HASH
from pyrogram import Client, enums
import time

app = Client("my_account", API_ID, API_HASH)


@app.on_message()
async def my_handler(client, message):
  await client.send_message("me", 'username')


async def main():
  async with app:
    while True:
      try:
        with open('Output.txt') as f:
          lines = f.readlines()
          if (len(lines)):
            await app.send_chat_action(lines[0], enums.ChatAction.TYPING)
        time.sleep(6)
      except Exception as e:
        time.sleep(60)
        print(e)


app.run(main())
