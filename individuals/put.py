import requests
username = 'joe'
userage = 41
url = 'https://old-voice-6624.getsandbox.com:443/users/'+username
obj = {
    'username': username,
    'age': userage
}
response = requests.put(url, data=obj)
output = response.json()
print(output)
