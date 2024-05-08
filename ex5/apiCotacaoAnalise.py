from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)


def get_exchange_rates():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        filtered_data = list(map(lambda x: {
            'name': data[x]['name'], 'high': data[x]['high'], 'low': data[x]['low']}, data.keys()))
        return filtered_data

    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"Erro ao obter dados da API: {err}")


@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        exchange_rates = get_exchange_rates()
        return jsonify(exchange_rates), 200
    except RuntimeError as err:
        return jsonify({"error": str(err)}), 500


if __name__ == '__main__':
    app.run(debug=True)
