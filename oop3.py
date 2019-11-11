class Animal():
    total_no_of_animal = 4
    print("the total number of animals inside ANIMAL", total_no_of_animal)
    def a1(self):
        print("the total number of animals ", self.total_no_of_animal)

class Bird(Animal):
    print("the total number of animals inside BIRD ", Animal().total_no_of_animal)

class parrot(Bird):
    print("the total number of animals inside PARROT ", Animal().total_no_of_animal)
    


o = parrot()

