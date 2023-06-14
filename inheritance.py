class Plane:
    def __init__(self, no_of_wings):
        self.no_of_wings=no_of_wings
    def  fly(self):
        if self.no_of_wings==2:
            ("should be able to fly")
class Jet(Plane):
  
    def __init__(self, color):
        self.color=color #blue
    def  show1(self):
        print(self.color)
class Passenger(Plane):
    def __init__(self, color):
        self.color=color #red
    def  show2(self):
        print(self.color)
obj1=Jet("blue")
obj2=Passenger("red")
obj3=Plane(2)
obj1.show1()
obj2.show2()
obj3.fly()