import requests

http_response = requests.get('http://127.0.0.1:8000/api/home')
if http_response:
    print(http_response.text)
else:
    print('Response is empty')