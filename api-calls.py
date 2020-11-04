import requests
username = 'joe'
userage = 41
url = 'https://old-voice-6624.getsandbox.com:443/users'
obj = {
    'username': username,
    'age': userage
}
def getUsers(getUrl):
    response = requests.get(getUrl)
    output = response.json()
    print(output)

def addUser(postUrl, postData):
    response = requests.post(postUrl, data=postData)
    output = response.json()
    print(output)

def editUser(editUrl, editData):
    editUrl = editUrl+'/'+username
    response = requests.put(editUrl, data=editData)
    output = response.json()
    print(output)

def delUser(delUrl, username):
    delUrl = delUrl+'/'+username
    response = requests.delete(delUrl)
    output = response.json()
    print(output)


#print("Adding Users")
#addUser(url, obj)
#print("Edit User")
#editUser(url, obj)
#print("Delete User"+username)
#delUser(url, username)
#print("Getting Users")
getUsers(url)
