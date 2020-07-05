import random
n=int(input())
k=int(input())
results=[]
source=[]
counts=1
for i in range(1,n+1):
    source.append(i)
    counts=counts*i
j=0
while j<counts:
    temp1=''
    temp2=list(source)
    while len(temp2)>0:
        temp3=random.choice(temp2)
        temp1=temp1+str(temp3)
        temp2.remove(temp3)
    if results.count(temp1)==0:
        results.append(temp1)
        j=j+1
results=sorted(results)
print(results[k-1])