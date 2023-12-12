import requests
from pprint import pprint
import os
_print = print
url = 'http://localhost:3001/tokens'

user_data = {
    "email":"luizotavio@gmail.com",
    "password":"123456"
}

response = requests.post(url=url, json=user_data)
if response.status_code >= 200 and response.status_code<=299:
    os.system('cls')
    print("Status code",response.status_code)
    print("Reason",response.reason)
    
    response_data = response.json()
    token=response_data["token"]
    
    with open('token.txt', 'w') as file:
        file.write(token)
    
    
    
else:
    os.system('cls')
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)