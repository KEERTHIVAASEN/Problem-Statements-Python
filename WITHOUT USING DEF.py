class op:
   def Operation(a,b,c):
        if c=='+':
            return a+b
        elif c=='-':
            return a-b
        elif c=='*':
            return a*b
        elif c=='/':
            return a/b
        else:
            return "i"
print("Enter Two Numbers: ", end="")
nOne = int(input("\n""Enter any No:"))
nTwo = int(input("Enter any No:"))
print('\n'"The Operators And the Values:", end="")
print("\n""*****************************")
print("\n""ADDIITION RESULT=",('+'(nOne,nTwo)))
print("SUBTRACTION RESULT=",(-(nOne,nTwo)))
print("MULTIPLICATION RESULT=",('*'(nOne,nTwo)))
print("DIVISION RESULT=",('/'(nOne,nTwo)))

print("Enter Two Numbers: ", end="")
nOne = int(input("\n""Enter any No:"))
nTwo = int(input("Enter any No:"))
print('\n'"The Operators And the Values:", end="")
print("\n""*****************************")
ch=input()
t=op()
res=t.Operation(nOne,nTwo,ch)
if res=="i":
    print("\nInvalid Operator")
else:
    print("\nResult=",res)

