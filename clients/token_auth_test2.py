import requests
from pprint import pprint

#{'key': '6abb592141422b8678df5bffb10353ef849a8da9'}

def client():

    token = 'Token 6abb592141422b8678df5bffb10353ef849a8da9'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        headers=headers
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
