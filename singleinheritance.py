class Box:
    def __init__(self,nameofStudent,rollNo):
        self.name =nameofStudent
        self.rollNo=rollNo

class Box2(Box):
    def __init__(self,name,rollNo,marks):
        self.marks=marks
        Box.__init__(self,"Raj",23)

obj2 =Box2("Shiv",23,99)
print(obj2.marks)
print(obj2.name)
print(obj2.rollNo)
