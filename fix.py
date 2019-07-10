from pyrogram import Client, Filters
app = Client("ssssn",bot_token="859744901:AAEm_YyLvVTkj3LrecJtnmZJ81BibIaBC3E",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   
bullet = -1001378725482                                              

@app.on_message(Filters.chat(bullet))
def main(client, message):
  client.edit_message_text(-1001368865846,6080,"""India vs Newziland

Live Score:"""+ "**" + message.text + "**" )


app.run()
