class A():
    # global var
    a = 12
    b = 13
    print("outside a method and inside a class ---> a", a)

    # constructor ----> parameterized constructor
    def __init__(self,z):
        self.z = z
        
    def a1(self):
        a11 = 1200 # local var
        print("a value is",self.a)
        print("a1 is :", a11)
        
    
        
    def a2(self):
        a2 = 2000
        print("a2:  ", a2)
        print(" a is ",self.a)
        


obj = A(89)
print(obj.a)
print(obj.b)
print(obj.z)

obj.a1()
obj.a2()
