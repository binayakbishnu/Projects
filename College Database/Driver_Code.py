import Login
import Database_login

#Login.login()

username = input("Enter username: ") #username
result = Database_login.verifyusername(username)
if result != 0:
    password = input("Enter password: ") #password
    result = Database_login.verifypassword(password)

if result != 0:
    print("Login successfull")
    Login.login()

