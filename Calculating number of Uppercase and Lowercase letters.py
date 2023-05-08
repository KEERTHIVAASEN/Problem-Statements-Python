def countUpperAndLowerCase(string):
 upper=0
 lower=0
for i in string:
  if(i.islower()):
       lower=lower+1
  elif(i.isupper()):
       upper=upper+1
print("Calculating number of Uppercase and Lowercase letters")
print("*********************************************")
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)
string=input("Enter the string")
countUpperAndLowerCase(string)