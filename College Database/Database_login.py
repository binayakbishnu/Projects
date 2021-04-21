class logindetails():
    def __init__(self,usernames = "",passwords = ""):
        self.usernames = usernames
        self.passwords = passwords

#=============================

student1 = logindetails("1A","xyz%40")
student2 = logindetails("2A","abc%40")
student3 = logindetails("1B","lmn%40")
student4 = logindetails("3A","ghi%40")

faculty1 = logindetails("PHY-1001","aaa%10")
faculty2 = logindetails("PHY-1001","bbb%10")
faculty3 = logindetails("PHY-1001","ccc%10")
faculty4 = logindetails("PHY-1001","ddd%10")

studentlist = [] #list of student details
#adding details to list
studentlist.append(student1)
studentlist.append(student2)
studentlist.append(student3)
studentlist.append(student4)

facultylist = [] #list of student details
#adding details to list
facultylist.append(faculty1)
facultylist.append(faculty2)
facultylist.append(faculty3)
facultylist.append(faculty4)

#=============================

if __name__ == 'main':
    print("Database_login")

#=============================

def verifyusername(username):
    flag =0

    for i in studentlist:
        if username == i.usernames:
            flag =1

    for i in facultylist:
        if username == i.usernames:
            flag =1

    if flag ==0:
        print("Not found!!")
        return 0

def verifypassword(password):
    flag =0
    for i in studentlist:
        if password == i.passwords:
            flag =1

    for i in facultylist:
        if password == i.passwords:
            flag =1

    if flag==0:
        print("Incorrect!!")
        return 0

