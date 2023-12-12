import requests
from pprint import pprint
_print = print
url = 'http://localhost:3001/users'
user_data = {
    "nome":"Luiz otávio",
    "password":"123456",
    "email": "luizotavio@gmail.com"
}

response = requests.post(url=url, json=user_data)
if response.status_code >= 200 and response.status_code<=299:
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)
    print("Json",response.json())
else:
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)