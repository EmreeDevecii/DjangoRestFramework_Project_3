# kendi clientlerimizi(sunucuya login isteği) yazıyoruz auth testi için

import requests
from pprint import pprint

#{'key': '6abb592141422b8678df5bffb10353ef849a8da9'}

def client():
    credentials = {
        'username': 'testt',
        'password': 'deneme123' 
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
