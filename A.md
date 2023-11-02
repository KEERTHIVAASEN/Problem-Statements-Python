Basic I/O Programming
print("Basic I/O programming")
print("*********************")
n = int(input("enter no of processes:"))
print("No of Processes=",n)
a_time = []
b_time = []
for x in range(n):
 print("enter the arrival time of process p{}".format(x+1))
 a = int(input())
 a_time.append(a)
print("arrival time of the processes:",a_time)
for x in range(n):
 print("enter the burst time of process p{}".format(x+1))
 a = int(input())
 b_time.append(a)
print("burst time of the processes:",b_time)
print("Pno\t\t AT\t\t BT")
for i in range(n):
 print("p{}".format(i+1),"\t\t",a_time[i],"\t\t",b_time[i])


Shortest Job First Scheduling Algorithm
print('Shortest Job First Scheduling Algorithm')
print('****************************************')
n = int(input('enter no of processes:'))
total = 0
process = [0] * n
bt = [0] * n
wt = [0] * n
tat = [0] * n
for i in range(n):
 print("P" + str(i + 1))
 bt[i] = int(input('Enter burst time:'))
 process[i] = i+1
for i in range(n):
 pos = i
 for j in range(i+1,n):
 if bt[j] < bt[pos]:
 pos = j
process = [i for _i in sorted(zip(bt,process))]
bt = [i for _,i in sorted(zip(process,bt))]
print(process,bt)
#first process has waiting time 0
wt[0] = 0
#calculate waiting time
for i in range(1,n):
 wt[i]=0
 for j in range(i):
 wt[i] += bt[j]
total += wt[i]
#calculating average waiting time
wait_avg = total/n
total = 0
print('\n Pno BT WT TAT')
for i in range(n):
 tat[i] = bt[i] + wt[i]
 total += tat[i]
 print('\n', process[i],' ',bt[i],' ',wt[i],' ',tat[i])
tat_avg = total/n
print('Average Waiting Time:%0.2f ms' %(wait_avg))
print('Average Turn Around Time:%0.2f ms' %(tat_avg))


FIRST COME FIRST SERVE SCHEDULING
print("FIRST COME FIRST SERVE SCHEDULING")
n= int(input("Enter number of processes : "))
d = dict()
for i in range(n):
key = "P"+str(i+1)
a = int(input("Enter arrival time of process"+str(i+1)+": "))
b = int(input("Enter burst time of process"+str(i+1)+": "))
l = []
l.append(a)
l.append(b)
d[key] = l
d = sorted(d.items(), key=lambda item: item[1][0])
CT = []
for i in range(len(d)):
# first process
if(i==0):
 CT.append(d[i][1][1])
# get prevCT + newBT
else:
 CT.append(CT[i-1] + d[i][1][1])
TAT = []
for i in range(len(d)):
TAT.append(CT[i] - d[i][1][0])
WT = []
for i in range(len(d)):
WT.append(TAT[i] - d[i][1][1])
avg_WT = 0
for i in WT:
avg_WT +=i
avg_WT = (avg_WT/n)
avg_TAT = 0
for i in TAT:
avg_TAT +=i
avg_TAT = (avg_TAT/n)
print("Pno AT BT CT TAT WT")
for i in range(n):
print(d[i][0]," ",d[i][1][0]," ",d[i][1][1]," ",CT[i]," ",TAT[i]," ",WT[i]," ")
print("Average Waiting Time:%0.2f ms " %(avg_WT))
print("Average Turn Around Time:%0.2f ms " %(avg_TAT))


FIRST IN FIRST OUT PAGE REPLACEMENT ALGORITHM
from queue import Queue
def pageFaults(pages, n, capacity):
 s = set()
 indexes = Queue()
 page_faults = 0
 for i in range(n):
 if (len(s) < capacity):
 if (pages[i] not in s):
 s.add(pages[i])
 page_faults += 1
 indexes.put(pages[i])
 else:
 if (pages[i] not in s):
 val = indexes.queue[0]
 indexes.get()
 s.remove(val)
 s.add(pages[i])
 indexes.put(pages[i])
 page_faults += 1
 return page_faults
# Driver code
pages = [7, 0, 1, 2, 0, 3, 0,4, 2, 3, 0, 3, 2]
n = len(pages)
capacity = 4
pf = pageFaults(pages, n, capacity)
fault_ratio = pf/n * 100
page_hit = n - pf
hit_ratio = page_hit/n * 100
print('total no of page fault=',pf)
print('fault ratio=%0.2f' %fault_ratio)


Least Recently Used Page Replacement
Algorithm

print('Least Recently Used Page Replacement Algorithm')
print('**********************************************')
capacity = int(input('enter the no of free frames:'))
processList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
s = []
pageFaults = 0
for i in processList:
 if i not in s:
 if (len(s) == capacity):
 s.remove(s[0])
 s.append(i)
 else:
 s.append(i)
 pageFaults += 1
 else:
 s.remove(i)
 s.append(i)
print("Total no of Page faults = {}".format(pageFaults))
fault_ratio = pageFaults/len(processList) * 100
page_hit = len(processList) - pageFaults
hit_ratio = page_hit/len(processList) * 100
print('fault ratio=%0.2f' %fault_ratio)
print('hit ratio=%0.2f' %hit_ratio)


Worst Fit
def worstFit(blockSize, m, processSize, n):
 allocation = [-1] * n
 for i in range(n):
 wstIdx = -1
 for j in range(m):
 if blockSize[j] >= processSize[i]:
 if wstIdx == -1:
 wstIdx = j
 elif blockSize[wstIdx] < blockSize[j]:
 wstIdx = j
 if wstIdx != -1:
 allocation[i] = wstIdx
 blockSize[wstIdx] -= processSize[i]
 print("PNo. Psize Block no.")
 for i in range(n):
 print(i + 1, " ",processSize[i], end = " ")
 if allocation[i] != -1:
 print(' ',allocation[i] + 1)
 else:
 print("Not Allocated")
#main driver code
print('Worst Fit Algorithm')
print('*******************')
blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)
worstFit(blockSize, m, processSize, n)
print('hit ratio=%0.2f' %hit_ratio**)
