n=int(input())
start=int(input())
numlist=[]
for i in range(pow(2,n)):
    numlist.append(i^i>>1)
index=numlist.index(start)
temp=numlist[index:]+numlist[0:index]
print(temp)