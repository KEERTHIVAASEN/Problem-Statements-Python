n1=0
n2=1
for count in range(6):
    print(n1,end=" ")
    next=n1+n2
    n1=n2
    n2=next
    count+=1
