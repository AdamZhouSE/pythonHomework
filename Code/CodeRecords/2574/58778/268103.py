n=int(input())
numlist=[]
for i in range(n):
    m=int(input())
    numlist.append(m)
primelist=[2]
n=3
while(len(primelist)!=max(numlist)):
    j=0
    for i in range(2,n):
        if(n%i==0):
            j=1
            break
    if(j==0):
        primelist.append(n)
    n=n+1
#print(primelist)
for c in numlist:
    print(1+primelist[c-1]**2)