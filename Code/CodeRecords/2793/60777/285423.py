temp=[int(x) for x in input().split(' ')]
n=temp[0]
c=temp[1]

ty=[int(x) for x in input().split(' ')]

count=1

for i in range(1,len(ty)):
    if((ty[i]-ty[i-1])<=c):
        count+=1
    else:
        count=1
if(c==0):
    count=0
print(count)