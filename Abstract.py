# Define an abstract class with a method
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Define a concrete subclass that implements the abstract method
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Method implementation in concrete class")

# Create an instance of the concrete subclass and call the method
obj = ConcreteClass()
obj.abstract_method()  # Output: Method implementation in concrete class
