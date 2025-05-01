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


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject):
        
        Student.__init__(self, name, age, student_id)
        
        Teacher.__init__(self, name, age, subject)

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)
        print("Subject:", self.subject)


ta1 = TeachingAssistant("Alex", 24, "ST1023", "ComputerScience")


ta1.show_details()





