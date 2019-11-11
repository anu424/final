print("NO PARAMETER no return type")
def method1():
    print("start")
    print("it's python class")
    print("end")
print("After method")
method1()


# with parameter without return typr
def addition(a,b):
    print("VAlue of A",a)
    print("VAlue of B",b)
    sum = a+b
    print("sum of 2 values:", sum)

addition(1,2)
addition(5,7)


# with parameter and with return type
def multiplication(a,b):
    result = a*b
    print("the result inside method", result)
    return result
res = multiplication(2,3)
print("the result outside method ", res)
    
# NO parameter with return type
def sample():
    return 1
a = sample()
print(a)



#a1,a2 = 12,13
#a1,a2 = a2,a1
a1 =10
a2 =  20
temp = a1
a1 = a2
a2 = temp 
print(" a1",a1,"a2",a2)




for i in range(10):
    print(i)
    if i == 5:
        break

print("--------------")
for i in range(10):
    if i%2== 0:
        continue
    print(i)


print(" LIST COMPREHENSION")
result = [ i for i in range(0,10)]
print(result)




print("--------------")
for i in range(0,10):
    print(i)












