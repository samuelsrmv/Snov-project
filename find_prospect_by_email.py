import requests
import json
from token_snov import get_access_token


def getProspectsByEmail(email):
    token = get_access_token()
    params = {'access_token':token,
            'email':email
    }

    res = requests.post('https://api.snov.io/v1/get-prospects-by-email', data=params)
    print(res)
    try:
        x = json.loads(res.text)
        return x
    except:
        return False
    


if __name__ == '__main__':
    getProspectsByEmail()