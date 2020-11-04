import requests
username = 'dave'
url = 'https://old-voice-6624.getsandbox.com:443/users/'+username
response = requests.delete(url)
output = response.json()
print(output)
