
class Dog(): 

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

    def bark(self):
        print("WOOF! My name is {}").format(self.name))

my_dog = Dog(breed='lab',name='Sammy')
my.dog.bark()

class Circle():

    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am dog!")

    def bark(self):
        print("WOOF!")


mydog.eat()
mydog.who_am_i()

# Polymorphism

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")

for pet in [niko,felix]:

    print(type(pet))
    print(pet.speak())

# instead of polymorphism, it's more common to use abstract classes (classes that will not be instantiated) as base for subclasses.

class Animal(): 

    def.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstracted method")

class Dog(Animal):

    def speak(self):
        return self.name+ "says woof!"

class Cat(Animal):

    def speak(self):
        return self.name+ "says meow!"

fido = Dog("Fido")
print(fido.speak())

#Special (Magic/Dunder) Methods

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")






