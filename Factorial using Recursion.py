def fact(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact(n-1)
print("Factorial using Recursion")
print("*************************")
n=int(input("Enter the number"))
print("The factorial of",n,"is",fact(n))