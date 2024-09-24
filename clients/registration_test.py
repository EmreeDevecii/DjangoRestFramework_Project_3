# kendi clientlerimizi(sunucuya login isteği) yazıyoruz auth testi için

import requests
from pprint import pprint

#{'key': '6abb592141422b8678df5bffb10353ef849a8da9'}

def client():
    credentials = {
        'username': 'rest_testt_user3',
        'email': 'test3@test.co',
        'password1': 'deneme12344', 
        'password2': 'deneme12344', 
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()