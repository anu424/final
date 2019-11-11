
"""
==,!=,< , > , <=, >= (Relational , comparsion operators)

= (a =10)
== (a == 10)

& -bitwise AND operator
| =OR
~ = XOR
<< bitwise leftshift
>> rightshift
4 =     8421
        0100
4>>1

0100
1000 = 8

MEMBERSHIP OPERATORS

a = [1,2,3,4,5,6]
print(6 in a)
print(7 in a)
print(7 not in a)


#Identity operator
b = [1,2,45]
print(id(b))
c = b
print(b)
print(c)
print(b is c)
d = a
print(d is not  c)


control flow
1. if
2. if else
3. if else ladder
4. nested  if


a = 12
b = 13
if  a == b:
    print(" a is equal to b")
else:
    print("a is not equal to b")


if a != 200: #12!=200
    print("a is 12")


if a > 0: #12>0
    print("outer if-loop---> true block")
    if a==b: #12==13
        print("nested true block")
    else:
        print(" nested false block")
else:
    print("outer if -loop ---> false block")
        



a=11
b=12
c=13

if (a>  0):
    if a> b:# 11 > 12
        print("a is greater than b")
    elif a> c:#11> 13
        print(" ais greater than c")
    elif (b> a): #12> 11
        print("b is greater than a")
    elif  b> c: # 12> 13
        print( " b is greater than c")
    elif (c> a):# 13> 11
        print("c is greater than a")
    else:
        print("c is greater thn b")
"""

# looping statement:
 #for ,while

l = [1,2,3,4,5]
a =100
for i  in l: 
    print("hi", i)


    

print("------------------")

for i in range(20):
    print(i)

print("------------------")
for i in range(5,11,2):
    print(i)

print("------------------")
for i in range(10,100):
    if i % 2 != 0:
        print(i,"is odd")

print("------------------")

for i in range(10,100,2):
    print(i)
    
    


print("------------------")

a =1
while a<=5:#1<=5 
    print(a)
    a+=1
print("------------------")

   

n =10 #1+2+3+....+10
sum = 0
while n >= 1:
    sum = sum+n
    n -=1
print(sum)

print("------------------")

fact=5
product=1
while fact >= 1:
    product = product* fact # product =1*5
    fact-=1
    print(product)
print(product)
    
    
    






















