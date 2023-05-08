print("FIBONACCI SERIES")
print("******************")
n=int(input("\nEnter the number of terms: "))
count=0
n1=0
n2=1
while(count<n):
 print(n1,end=" ")
next=n1+n2
n1=n2
n2=next
count+=1