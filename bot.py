import os
from pyrogram import Client, filters

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

canal_origen = "bsc_tokens"
canal_destino = "mistokens"
tokens_a_detectar = ["FOUR", "ZHAO", "FOURDOTDEX"]

app = Client("mi_userbot", api_id, api_hash)

@app.on_message(filters.chat(canal_origen))
async def filtrar_tokens(client, message):
    if not message.text:
        return

    texto = message.text.upper()

    for token in tokens_a_detectar:
        if token in texto:
            await message.forward(canal_destino)
            print(f"[ENVIADO] {token}")

app.run()
