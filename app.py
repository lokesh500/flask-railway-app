from flask import Flask, request
import requests

app = Flask(name)

# Lokesh Sir ka Telegram Bot Token
BOT_TOKEN = '7753236397:AAFpv1zb-HK-feQzVSx4qGbEOG4Z6ek1pRA'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return "✅ Lokesh ka Telegram Bot is LIVE!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_text = data['message'].get('text', '')

        reply_text = f"Aapne bola: {message_text}"

        # Send reply back to Telegram
        requests.post(TELEGRAM_API_URL, data={
            'chat_id': chat_id,
            'text': reply_text
        })

    return "ok", 200
