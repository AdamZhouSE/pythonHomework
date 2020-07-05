s1 = input().split(' ')
n = int(s1[0])
m = int(s1[1])
nums =[]
for i in range(0,n):
    s = input().split(' ')
    for i in range(1,int(s[0])+1):
        nums.append(int(s[i]))

nums = list(set(nums))
target =[]

for i in range(0,m):
    target.append(i+1)

if target == nums:
    print("YES")
else:
    print("NO")