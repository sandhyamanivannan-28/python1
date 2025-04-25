# class school:
#     def __init__(self,name,reg_no,subject):
#        self.name=name
#        self.reg_no=reg_no
#        self.subject=subject
#        print("the student details") 
# class student(school):
#     def __init__(self,name,reg_no,subject):
#          super().__init__(name,reg_no,subject)   
#          print("student constructor") 
# student1=student("natasha",1256,"accounts")
# print(student1.name)     
# print(student1.reg_no)
# print(student1.subject)


class office_details:
    def __init__(self,name,id_no,salary,deparatment):
        self.name=name
        self.id_no=id_no
        self.salary=salary        
        self.department=deparatment
class empolyee(office_details):
    def __init__(self,name,id_no,salary,deparatment):
        super().__init__(name,id_no,salary,deparatment)
empolyee1=empolyee("natasha",35467,68.000,"analyts")
print(f"name of the empolyee : { empolyee1.name}")
print(f"empolyee id_n:{empolyee1.id_no}")
print(f"salary ammount:{empolyee1.salary}")
print( f"department:{empolyee1.department}")
print("-------------------------------------------------")
empolyee2=empolyee("arjun",65247,88.000," senior_1 analyts")
print(f"name of the empolyee : {empolyee2.name}")
print(f"empolyee id_n:{empolyee2.id_no}")
print(f"salary ammount:{empolyee2.salary}")
print(f"department:{empolyee2.department}")
print("-------------------------------------------------")
empolyee3=empolyee("sam",68579,98.000," senior_1 analyts")
print(f"name of the empolyee : {empolyee3.name}")
print(f"empolyee id_n:{empolyee3.id_no}")
print(f"salary ammount:{empolyee3.salary}")
print(f"department:{empolyee3.department}")
print("-------------------------------------------------")
empolyee4=empolyee("keerthi",67447,94.000," senior_2 analyts")
print(f"name of the empolyee : {empolyee4.name}")
print(f"empolyee id_n:{empolyee4.id_no}")
print(f"salary ammount:{empolyee4.salary}")
print(f"department:{empolyee4.department}")
print("-------------------------------------------------")
empolyee5=empolyee("varun",65647,78.000," senior_3 analyts")
print(f"name of the empolyee : {empolyee5.name}")
print(f"empolyee id_n:{empolyee5.id_no}")
print(f"salary ammount:{empolyee5.salary}")
print(f"department:{empolyee5.department}")
print("-------------------------------------------------")
        



               
        


