import requests
import json
from token_snov import get_access_token

def add_prospect_list():
    token = get_access_token()
    params = {
        'access_token':token,
        'name':'Campaña de Pruebas'
    }
    
    res = requests.post('https://api.snov.io/v1/lists', data=params)
    print(res)
    x = json.loads(res.text)
    print(x)
    return json.loads(res.text)

if __name__ == '__main__':
    add_prospect_list()

    