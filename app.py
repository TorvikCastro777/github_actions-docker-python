from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>💰 Cripto-Torvik 💰</h1>
    <p>Bienvenido a tu primer servicio financiero.</p>
    <p>Visita <a href="/bitcoin">/bitcoin</a> para ver el precio actual.</p>
    '''

@app.route('/bitcoin')
def get_bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']
    return jsonify({
        'moneda': 'Bitcoin (BTC)',
        'precio_usd': price,
        'mensaje': '¡Torvik to the moon! 🚀'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
