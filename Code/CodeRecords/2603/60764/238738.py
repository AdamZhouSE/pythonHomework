import re
n=list(map(int,re.sub("\D"," ",input()).split()))
k=int(input())
dislist=[]
for i in range(len(n)-1):
    j=i+1
    while j<len(n):
        dislist.append(abs(n[i]-n[j]))
        j+=1
dislist.sort()
print(dislist[k-1])