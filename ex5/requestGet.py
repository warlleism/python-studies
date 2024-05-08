import requests

url = 'https://jsonplaceholder.typicode.com/posts'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Erro: ", response.status_code)
except Exception as erro:
    print("Error: ", erro)
