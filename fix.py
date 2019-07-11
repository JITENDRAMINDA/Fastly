from pyrogram import Client, Filters
app = Client("ssssn",bot_token="859744901:AAEm_YyLvVTkj3LrecJtnmZJ81BibIaBC3E",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   
bullet = -1001378725482                                              

@app.on_message(Filters.chat(bullet) & ~ Filters.edited)
def main(client, message):
  if "🚾" in message.text:
   client.edit_message_text(-1001368865846,6143,"""♻️ __England vs Australia__

**Live Score** : """+ " " + message.text )
  elif "📟" in message.text:
   client.edit_message_text(-1001368865846,6143,"""♻️ __England vs Australia__

**Live Score** : """+ " " + message.text )
  elif "WKT" in message.text:
    client.edit_message_text(-1001368865846,6143,"""♻️ __England vs Australia__

**Live Score** : """+ " " + message.text )
  elif "WIN" in message.text:
    client.edit_message_text(-1001368865846,6143,"""♻️ __England vs Australia__

**Live Score** : """+ " " + message.text )
 
  elif "🎾" in message.text:
    client.edit_message_text(-1001368865846,6143,"""♻️ __England vs Australia__

**Live Score** : """+ " " + message.text )




app.run()
