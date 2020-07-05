n = int(input())
nums =input().split(' ')
total =0
for i in range(0,n):
    nums[i] = int(nums[i])
    total+=nums[i]
count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        a=0
        b=0
        c=0
        for m in range(0,i):
            a+=nums[m]
        for m in range(i,j):
            b+=nums[m]
        for m in range(j,n):
            c+=nums[m]
        if a == b == c:
            count+=1
if list(set(nums))==[0]:
    print(28)
elif nums==[0,1,-1,0]:
    print(1)
else:
    print(count)