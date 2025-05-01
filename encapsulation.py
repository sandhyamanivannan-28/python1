# class car:
#     brand="ford"
# car1=car()
# print(car1.brand)   


class empolyee:
    def __init__(self):
        self._salary=980000
class manager(empolyee):
    def manager(self):
        print(self._salary)
empolyee1=manager()
empolyee1.manager()