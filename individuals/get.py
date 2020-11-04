import requests

url = 'https://old-voice-6624.getsandbox.com:443/users'
response = requests.get(url)
output = response.json()
print(output)
