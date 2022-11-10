import requests
import json
from find_prospect_by_email import getProspectsByEmail
from token_snov import get_access_token


def change_recipient_status(email, campaign_id, status_campaing):
    #print("***************************************")
    # print(email)
    # print(campaign_id)
    # print(status_campaing)
    # print("***************************************")
    token = get_access_token()
    params = {'access_token':token,
            'email': email,
            'campaign_id': campaign_id,
            'status': status_campaing
    }

    res = requests.post('https://api.snov.io/v1/change-recipient-status', data=params)
    print(res)
    try:
        return json.loads(res.text)
    except:
        pass

if __name__ == '__main__':
    change_recipient_status()