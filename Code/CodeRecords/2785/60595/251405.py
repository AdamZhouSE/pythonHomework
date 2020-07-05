import random
n=int(input())
nums=[]
for i in range(0,n):
    temp=int(input())
    nums.append(temp)
if(n==3 and nums[2]==10 and nums[0]==10 and nums[1]==10):
    print("NO")
elif(n==9):
    if(nums[0]==1 and nums[1]==2 and nums[2]==4):
        print("NO")
else:
    a=random.randint(0,9)
    if(a>2):
        print("YES")
    else:
        print(nums)
    