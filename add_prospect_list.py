import requests
import json
from token_snov import get_access_token


def add_prospect_to_list():
    token = get_access_token()
    params = {'access_token':token,
            'email':'john.doe@example.com',
            'fullName': 'Samu pruebaa',
            'firstName':'Samu',
            'lastName':'pruebaa',
            'country':'United States',
            'locality':'1',
            'socialLinks[linkedIn]':'https://www.linkedin.com/in/johndoe/&social',
            'social[twiiter]':'https://twitter.com/johndoe&social',
            'position':'Vice President of Sales',
            'companyName':'GoldenRule',
            'companySite':'https://goldenrule.com',
            'updateContact':1,
            'listId':'11925773'
            
    }

    res = requests.post('https://api.snov.io/v1/add-prospect-to-list', data=params)
    print(res)
    print(json.loads(res.text))

if __name__ == '__main__':
    add_prospect_to_list()