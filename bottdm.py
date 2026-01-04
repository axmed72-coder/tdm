from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("8462126131:AAHX9lknojLex-N3Pq10AP-VBIy0f5XsXTg")
CHAT_ID = os.getenv("8344514260")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    text = f"""з
📩 Новая заявка
👤 Имя: {data.get('name')}
📞 Контакт: {data.get('contact')}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
