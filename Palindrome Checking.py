print("Palindrome Checking")
print("******************")
str1=input("Enter a String:")
str2=""
for i in str1:
 str2=i+str2
 if str1==str2:
      print("Palindrome")
      break
else:
 print("Not a Palindrome")