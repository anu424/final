print(" ----hierarchical-----------")
class A:
    a = 89
    def A1(self):
        print("inside SUPER class")
        
class B(A):
    b = 23
    def B1(self):
        print("iside SUBCLASS-1 ")

class C(A):
    c = 12
    def C1(self):
        print("inside SUBCLAS_2")
    
        

class D(A):
    d = 234
    def d1(self):
        print("inside SUBCLAS_3")


o = D()
print(o.d)
print(o.a)
o.d1()
o.A1()
