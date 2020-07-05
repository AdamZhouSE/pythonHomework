t=int(input())
nums=[]
for i in range(t):
    nums.append(int(input()))
for i in range(t):
    if(nums[i]%2==0):
        print("1")
    else:
        print("0")