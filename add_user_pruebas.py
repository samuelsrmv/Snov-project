import requests
import json
import csv
from token_snov import get_access_token


def add_prospect_to_list():
    
    f_id_1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget dolor morbi non arcu risus quis varius quam. Suspendisse faucibus interdum posuere lorem. Justo donec enim diam vulputate. """

    token = get_access_token()
    params = {'access_token':token,
            'email':'samuel.srmv@gmail.com',
            'fullName': 'Francisco Doe',
            'firstName':'Francisco',
            'lastName':'Doe',
            'country':'United States',
            'locality':'Woodbridge, New Jersey',
            'socialLinks[linkedIn]':'https://www.linkedin.com/in/johndoe/&social',
            'social[twiiter]':'https://twitter.com/johndoe&social',
            'position':'Vice President of Sales',
            'companyName': 'Ayenda SAS',
            'companySite':'https://goldenrule.com',
            'updateContact':1,
            'customFields[f_id_1]': f_id_1,
            'listId':'10706920'
    }
    res = requests.post('https://api.snov.io/v1/add-prospect-to-list', data=params)
    print(json.loads(res.text))
    return json.loads(res.text)   
    
if __name__ == '__main__':
    add_prospect_to_list()
