import requests
username = 'dave'
usermail = 'john@mail.com'
url = 'https://old-voice-6624.getsandbox.com:443/users'

def setObj(username):
    print("Creating user named: "+username)
    obj = {
        'username': username,
        'mail': username+'@mail.com'
    }
    return obj

def changeObj(username, email):
    obj = {
        'username': username,
        'mail': email
    }
    return obj

def getUsers(getUrl):
    response = requests.get(getUrl)
    output = response.json()
    print(output)

def addUser(postUrl):
    username = str(input("Enter User Name to Add: "))
    postData = setObj(username)
    q = { 'username': username}
    response = requests.post(postUrl, data=postData)
    output = response.json()
    print(output)

    q = { 'username': username}
    req = requests.get(postUrl, params=q)
    print("The user is added!")
    print(req.text)

def editUser(editUrl):
    username = str(input("Enter User Name to Edit: "))
    editUrl = editUrl+'/'+username
    query = { 'username': username}
    req = requests.get(editUrl, params=query)
    print("The user available is:")
    print(req.text)
    
    print("Select Parameter to Edit\n1. Username\n2. Email")
    i = int(input("Enter your Choice: "))

    if i == 1:
        username = str(input("Enter New Username: "))
    elif i == 2:
        mail = str(input("Enter New Mail: "))
    else:
        print("Wrong Choice")

    editData = changeObj(username,mail)

    response = requests.put(editUrl, data=editData)
    output = response.json()
    print(output)

    req = requests.get(editUrl, params=query)
    print("The user is updated!")
    print(req.text)

def delUser(delUrl):
    username = str(input("Enter Username to Delete: "))
    
    delUrl = delUrl+'/'+username
    getUsers(delUrl)
    confirm = str(input("Confirm record to delete (y/n): "))
    
    if confirm == 'y':
        response = requests.delete(delUrl)
        output = response.json()
        print(output)
        print("User Deleted!")
    elif confirm == 'n':
        print("Nothing Deleted")
    else:
        print("Wrong Choice!")

def switch():
    
    looper = True
    while looper == True:  
        print("Select your Choice:\n1. Create User\n2. Read Users\n3. Update User\n4. Delete User\n5. Exit")
        option = int(input("Enter your Choice: "))
        if option == 1:
            print("Adding Users")
            addUser(url)
        elif option == 2:
            print("Getting Users")
            getUsers(url)
        elif option == 3:
            print("Edit User")
            editUser(url)
        elif option == 4:
            print("Delete User")
            delUser(url)
        elif option == 5:
            print("Exiting...")
            looper = False
        else:
            print("Incorrect Choice, try again...")
        

switch()