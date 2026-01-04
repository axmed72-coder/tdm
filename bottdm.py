from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

# Telegram токен и чат ID из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Главная страница с формой
@app.route("/")
def index():
    return render_template("index.html")  # index.html должен лежать в папке templates/

# Endpoint для отправки заявки
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    text = f"""
📩 Новая заявка
👤 Имя: {data.get('name')}
📞 Контакт: {data.get('contact')}
"""

    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    
    return {"status": "ok"}

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


   
