print(" ----MULTIPLE----------")
class A:
    a = 89
    def A1(self):
        print("inside SUPER class---A")

class B:
    b = 89
    def B1(self):
        print("inside SUPER class ---B")
        
      
class C(A,B):
    c = 23
    def C1(self):
        print("iside SUBCLASS-1 ")

o = C()
print(o.a)
print(o.b)
print(o.c)
o.C1()
o.A1()
o.B1()
