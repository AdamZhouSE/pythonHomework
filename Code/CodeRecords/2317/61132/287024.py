import math

l=list(map(int,input().split(',')))
sum=0
l=sorted(l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        sum+=((l[j]-l[i])*math.pow(2,j-i-1))
print(int(sum%1000000007))