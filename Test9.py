class student:  
    def __init__(self, roolNumber,name, gpa, semester):  
        self.name = name  
        self.roolNumber = roolNumber 
        self.gpa =gpa
        self.semester = semester

list = []
list.append(student("20k-1409","Muhammad Asher Ansari","3.5",1))
list.append(student("20k-1409","Muhammad Asher Ansari","3.5",6))
list.append(student("20k-1409","Muhammad Asher Ansari","3.5",8))
list.append(student("20k-1409","Muhammad Asher Ansari","3.5",8))

for student in list:
    print(student.name + ", Semester: "+str(student.semester))