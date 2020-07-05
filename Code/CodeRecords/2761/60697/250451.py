t=int(input())
nums=[]
for i in range(t):
    nums.append(int(input()))
for i in nums:
    res=0
    for j in range(1,i+1):
        res+=j*j
    print(res)
    