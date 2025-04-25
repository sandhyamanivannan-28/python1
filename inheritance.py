# class person:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age
#    
# class work:
#    def __init__(self,position,salary):
#       self.position=position
#       self.salary=salary
# class employee(person,work):
#     def __init__(self,name,age,position,salary):
#        self.name=name
#        self.age=age
#        self.position=position
#        self.salary=salary
# person1=employee("natasha",28,"analysts",89.0000)
# print(f"name of the empolyee: {person1.name}")
# print(f"age of the empolyee: {person1.age}")
# print(f"position of the empolyee: {person1.position}") 
# print(f"salary of the empolye:{person1.salary}")        
        


# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# class car(vehicle):
#     def __init__(self,fuel_type):
#        self.fuel_type=fuel_type
# class electric_car(car):
#     def __init__(self,brand,model,fuel_type,battery_capacity):
#         self.brand=brand
#         self.model=model
#         self.fuel_type=fuel_type
#         self.battery_capacity=battery_capacity
# car1=electric_car("tata","suv23","battery","87mtz")
# print(car1.model)
# print(car1.battery_capacity)
# print(car1.brand)
# print(car1.fuel_type)



class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,student_id):
        self.student_id=student_id
        super().__init__(name, age)   
class teacher(person):
        def __init__(self, name, age,student_id,subject):
             self.subject=subject
             super().__init__(name, age,student_id)            
class teacher_assistant(student,teacher):
     def __init__(self,name,age,student_id,subject):
          super().__init__(name,age,student_id,subject)
assistant1=teacher_assistant("sam",29,"uk2509s22","computer")
print("the name :",assistant1.name)
print("the age is:",assistant1.age)
print("the student_id is :",assistant1.student_id)
print("the subject is :",assistant1.subject)


