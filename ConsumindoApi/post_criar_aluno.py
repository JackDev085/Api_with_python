import requests
from pprint import pprint
from get_token import token
_print = print
url = 'http://localhost:3001/alunos'

headers = {
    "Authorization" : token
}

aluno_data = {
	"nome": "Luana",
	"sobrenome": "Vieira",
	"email": "Luana@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}

response = requests.post(url=url, json=aluno_data, headers = headers)
if response.status_code >= 200 and response.status_code<=299:
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)
    print("Json",response.json())
else:
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)
