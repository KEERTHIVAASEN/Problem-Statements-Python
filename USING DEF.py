def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

print("Enter Two Numbers: ", end="")
nOne = int(input("\n""Enter any No:"))
nTwo = int(input("Enter any No:"))
print('\n'"The Operators And the Values:", end="")
print("\n""*****************************")
print("\n""ADDIITION RESULT=",(add(nOne,nTwo)))
print("SUBTRACTION RESULT=",(sub(nOne,nTwo)))
print("MULTIPLICATION RESULT=",(mul(nOne,nTwo)))
print("DIVISION RESULT=",(div(nOne,nTwo)))
