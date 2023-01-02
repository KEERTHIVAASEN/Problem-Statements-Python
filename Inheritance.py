# Define a base class with a method
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Define a subclass that inherits from the base class
class Dog(Animal):
    def make_sound(self):
        print("Labrador")

# Create an instance of the subclass and call its method
dog = Dog()
dog.make_sound() 
