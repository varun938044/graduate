
class Box:
    def __init__(self,nameofstudent,rollNO):
        self.name = nameofstudent
        self.rollNO = rollNO


class student:
    def __init__(self,fees):
        self.fees = fees
class Box2(Box,student):
    def __init__(self,name,rollNO,marks,fees):
        self.marks = marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollNO)

class Box3(Box2):
    def __init__(self,sem):
        self.sem = sem
        Box2.__init__(self,"vikram","07",33,22000)
obj = Box3("2-1")
print(obj.sem)
print(obj.name)

obj2 = Box2("simha","07",33,22000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.rollNO)

obj3 = Box2("damu",85,284,190000)
print(obj3.name)
print(obj3.rollNO)
print(obj3.marks)
print(obj3.fees)
