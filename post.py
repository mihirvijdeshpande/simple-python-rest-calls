import requests

url = 'https://old-voice-6624.getsandbox.com:443/users'
obj = {
    'username': 'joe',
    'age': 32
}
response = requests.post(url, data=obj)
output = response.json()
print(output)
