from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/posts', methods=['GET'])
def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return jsonify(data), 200
        else:
            return jsonify({"error": "Erro ao obter os posts"}), response.status_code
    except Exception as erro:
        return jsonify({"error": "Erro interno do servidor"}), 500


if __name__ == '__main__':
    app.run(debug=True)
