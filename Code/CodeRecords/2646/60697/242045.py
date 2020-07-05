t=int(input())
nums=[]
for i in range(t):
    nums.append(int(input()))
for i in range(t):
    l=nums[i]
    if(l%2==1):
        print("Player A")
    else:
        print("Player B")