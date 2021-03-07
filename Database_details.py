class Personal_Details:
    def __init__(self,name="",age=0,id=""):
        self.name = name
        self.age = age
        self.id = id

class Student(Personal_Details):
    def __init__(self,name="",age=0,id="",marks=[],avg=0.0):
        #Personal_Details.__init__(name,age,id)
        super().__init__(name,age,id)
        self.marks = marks
        self.avg = avg

    def print(self):
        print(self.name,self.age)

class Faculty(Personal_Details):
    def __init__(self,name,age,id,expyrs=0,dept=""):
        #Personal_Details.__init__(name,age,id)
        super().__init__(name,age,id)
        self.expyrs = expyrs
        self.dept = dept

#========================================

number=5
def details(object):
    print("Printing details...")
    print("Name: {}\nAge: {}\nID: {}".format(object.name,object.age,object.id))

def student_report(object):
    total = sum(object.marks)
    object.avg = total/number
    print("Name: {}".format(object.name))
    print("ID: {}".format(object.id))
    print("Marks: {}".format(object.marks))
    print("Average: {}".format(object.avg))

def faculty_report(object):
    #print("Printing department and experience...")
    print("Name: {}".format(object.name))
    print("ID: {}".format(object.id))
    print("Department: {}\nExperience: {} years".format(object.dept,object.expyrs))

#=======================================

mark = []
mark.append(30)
mark.append(35)
mark.append(42)
mark.append(38)
mark.append(45)
student1 = Student("Binayak",18,"1A",mark)

mark = []
mark.append(55)
mark.append(50)
mark.append(56)
mark.append(49)
mark.append(51)
student2 = Student("Bishnu",18,"2A",mark)

mark = []
mark.append(52)
mark.append(57)
mark.append(48)
mark.append(50)
mark.append(55)
student3 = Student("Neon",17,"1B",mark)

mark = []
mark.append(29)
mark.append(35)
mark.append(42)
mark.append(38)
mark.append(30)
student4 = Student("NeonX",18,"3A",mark)

faculty1 = Faculty("PHY-1001",48,"F1A",10,"Pure Science")
faculty2 = Faculty("CHY-1001",50,"F1B",12,"Pure Science")
faculty3 = Faculty("ITE-1001",45,"F1C",8,"Information Technology")
faculty4 = Faculty("CSE-1001",40,"F2C",10,"Computer Science")

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

'''Testing...
details(studentlist[1])
details(facultylist[2])

student_report(studentlist[1])
faculty_report(facultylist[2])
'''

def outputdetails(name):
    flag =0
    name=name.upper()
    
    for i in studentlist:
        
        if i.name.upper() == name:
            flag=1
            details(i)
    
    for i in facultylist:
        if i.name.upper() == name:
            flag=1
            details(i)
            
    if flag==0:
        print("Not found!!!")

def outputreport(name):
    flag=0
    name=name.upper()

    for i in studentlist:
        if i.name.upper() == name:
            flag=1
            student_report(i)
    
    for i in facultylist:
        if i.name.upper() == name:
            flag=1
            faculty_report(i)

    if flag==0:
        print("Not found!!!")
