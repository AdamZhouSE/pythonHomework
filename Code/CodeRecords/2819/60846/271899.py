n=int(input())
nums=[int(x) for x in input().split()]
dict={1:0,2:0}
cnt=0
for num in nums:
    if num==4:
        cnt+=1
    elif num==3:
        cnt+=1
        dict[1]-=1
    elif num==1:
        dict[1]+=1
    elif num==2:
        dict[2]+=1
dict[1]=max(0,dict[1])
import math
cnt+=math.ceil((dict[1]+2*dict[2])/4)
print(cnt)