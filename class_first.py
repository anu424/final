class pen():
    color = 'black'
    height = 5
    ink ='blue'
    brand = 'camlin'
    print("the pen color is ", color," and ink is ",ink )
    
    def writing(self):
        print("im writing")

    def throw(self):
        print(" i'll throw pen")

o = pen()
print(o.color)
print(o.ink)
print(o.brand)
o.writing()
o.throw()

