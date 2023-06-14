class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("the addition of two number is")
        print(self.n1+self.n2)
    def sub(self):
        print("the subtraction of two number is")
        print(self.n1-self.n2)
    def mul(self):
        print("the multiplication of two number is")
        print(self.n1*self.n2)
    def div(self):
        try:
            print("the division of two number is")
            print(self.n1/self.n2)
        except:
            print("division is not posibble")
    def mod(self):
        print("the modulo of two number is")
        print(self.n1%self.n2)
   
total=int(input("enter the number of entries "))
for j in range(total):
    n=input()
    count=0
    for i in range(len(n)):
        if n[i].isnumeric()!=True:
            count=i
    number1=int(n[0:count])
    number2=int(n[count+1:len(n)])
    obj1=Calculator(number1,number2)
    if n[count]=="+":
        obj1.add()
    elif n[count]=="-":
        obj1.sub()
    elif n[count]=="*":
        obj1.mul()
    elif n[count]=="/":
        obj1.div()
    elif n[count]=="%":
        obj1.mod()
    
        
    
    