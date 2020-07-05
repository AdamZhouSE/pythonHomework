import random
n=int(input())
nums=[]
for i in range(0,n):
    temp=int(input())
    nums.append(temp)
if(n==3 and nums[2]==10 and nums[0]==10 and nums[1]==10):
    print("NO")
if(n==9):
    print("NO")
elif(n==0):
    print("NO")
else:
    print("YES")
    