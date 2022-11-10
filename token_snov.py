import requests
import json

def get_access_token():
    params = {
        'grant_type': 'client_credentials',
        'client_id': '8b7a3c22694cc6429d86dd6a8ca4d750',
        'client_secret': '60bf8c1dd673509e0c1b31c1a0cebeee'
    }

    res = requests.post('https://api.snov.io/v1/oauth/access_token', data=params)
    print(res)
    resText = res.text.encode('ascii','ignore')
    
    try:
        return json.loads(resText)['access_token']
    except:
        pass
    

if __name__ == '__main__':
    get_access_token()

    