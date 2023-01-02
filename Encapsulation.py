# Define a class with private attributes and public methods
class EncapsulatedClass:
    def __init__(self):
        self.__private_attribute = 0

    def set_attribute(self, value):
        self.__private_attribute = value

    def get_attribute(self):
        return self.__private_attribute

# Create an instance of the class and call its methods
obj = EncapsulatedClass()
obj.set_attribute(10)
print(obj.get_attribute())  # Output: 10
