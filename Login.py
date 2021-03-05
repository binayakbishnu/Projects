import Database
print("Welcome to Login module\n")

def login():
    print("Welcome to college database\nChoose Student/Faculty: ")
    choice = input().upper()
    if choice == "Student".upper():   student()
    elif choice == "Faculty".upper():   faculty()

def choose_det_rep(name):
    print("1.Details\n2.Report\n1 or 2->")
    dr=int(input())
    if dr==1:
        Database.outputdetails(name)
    elif dr==2:
        Database.outputreport(name)
    #also reduces function call to the database to one place

def student():
    print("Opening student database...")
    time.sleep(2)
    name = input("Enter name: ")
    choose_det_rep(name)

def faculty():
    print("Opening faculty database...")
    time.sleep(2)
    name = input("Enter name: ")
    choose_det_rep(name)

if __name__ == '__main__':
    print("Module main body")

else:
    print("Initialising Login module...")
    import time
    time.sleep(2)   #2 seconds wait
    print("Initialised Login module\n")
    login()

