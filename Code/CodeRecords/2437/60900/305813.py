s =input().split(' ')
n =int(s[0])
q = int(s[1])
nums =input().split(' ')
for i in range(0,n):
    nums[i]=int(nums[i])
qs =[]
for i in range(0,q):
    qs.append(input().split(' '))
    qs[i][0]=int(qs[i][0])
    qs[i][1]=int(qs[i][1])

for i in range(0,q):
    print(min(nums[qs[i][0]-1:qs[i][1]]),end=' ')