temp=[int(x) for x in input().split(',')]

long=0
for i in range(len(temp)):
    pre=1
    maxi=temp[i]
    for j in range(i+1,len(temp)):
        if(temp[j]>maxi):
            maxi=temp[j]
            pre+=1
    if(pre>long):
        long=pre

print(long)
