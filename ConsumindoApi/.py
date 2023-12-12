# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests, requests_toolbelt

#Padrão de portas
# http:// -> 80
# https:// -> 443

url = 'http://localhost:8000/'
response = requests.get(url)    

print(response.status_code)

# print(response.headers)

#conteúdo do site em bytes
# print(response.content)

# print(response.json())
#Retorna o html do site
print(response.text)