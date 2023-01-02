# Define a base class with a method
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Define a subclass that inherits from the base class
class Dog(Animal):
    def make_sound(self):
        print("Labrador")

# Define another subclass that inherits from the base class
class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Create a list of objects
animals = [Dog(), Cat()]

# Call the method of each object in the list
for animal in animals:
    animal.make_sound()


