import requests
import json
from token_snov import get_access_token


def user_lists():
    token = get_access_token()
    params = {'access_token':token,
            'campaignId': 691329
    }

    res = requests.get('https://api.snov.io/v1/emails-sent', data=params)
    print(res)
    result = json.loads(res.text)
    return result


if __name__ == '__main__':
    user_lists()