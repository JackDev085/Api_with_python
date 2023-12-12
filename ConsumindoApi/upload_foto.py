import requests
from pprint import pprint
from get_token import token
from mimetypes import MimeTypes
import MultipartEncoder

_print = print
print = pprint

nome_arquivo = 'python_logo.png'
mimetypes = MimeTypes()
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)

multipart = MultipartEncoder(fields = {
    'aluno_id':'2',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)})
url = 'http://localhost:3001/fotos'


headers = {
    "Authorization" : token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers = headers,)
if response.status_code >= 200 and response.status_code<=299:
    
    response_data = response.json()
    print(response_data.status_code)
    print(response_data.reason)
else:
    print("Status code",response.status_code)
