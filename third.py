a = "hello1 "
print(a.isalpha())
a = "123 "
print(a.isdigit())

a = "as123 "
print(a.isalnum())

a = " "
print(a.isspace())

a = "hi hello"
print(a.isspace())

a = "python"
print(a.startswith('t'))
print(a.endswith('p'))

a = "python"
print(a.replace('t','p'))

a= "hello"
print(a.count('l'))
print(a[1])
print(a[-1])
print(a[0])
print(a[2])
print(a[3])
print(a[0:3])

print(a.index('l',3))

a = "this is python class"
print(a.split())

l = [1,2.34, 'hi']
l1 = [1,2,3,4,5]
print(l)
print(l[2])
print(l1[3])
l[1] = 5.67
print(l)


l.append(12)
print(l)

l.pop()
print(l)

l.remove(1)
print(l)
(l.insert(1,'python'))
print(l)








