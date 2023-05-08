l=[4,67,5,8,1,3,6,54,22,21,10]
evencount,oddcount=0,0
for n in l:
   if n%2==0:
     evencount=evencount+1
   else:
      oddcount+=1
print("Counting number of odd and even numbers")
print("***********************************")
print("Given List:",l)
print("Number of even numbers is",evencount)
print("Number of odd numbers is",oddcount)