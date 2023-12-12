import requests
from pprint import pprint
from get_token import token
_print = print
print = pprint
url = 'http://localhost:3001/alunos'

"""
aluno_data = {
	"nome": "Luana",
	"sobrenome": "Vieira",
	"email": "Luana@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}"""

response = requests.get(url=url)
if response.status_code >= 200 and response.status_code<=299:
    response_data = response.json()
    response.status_code
    response.reason
    
    for aluno in response_data:
        print(aluno)
        
    response.status_code
    response.reason

else:
    print("Status code",response.status_code)
    print("Reason",response.reason)
    print("Texto",response.text)
