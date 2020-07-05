
n =int(input())

nums =input().split(' ')
q =int(input())
for i in range(0,n):
    nums[i]=int(nums[i])
qs =[]
for i in range(0,q):
    qs.append(input().split(' '))
    qs[i][0]=int(qs[i][0])
    qs[i][1]=int(qs[i][1])

for i in range(0,q):
    
    print(len(list(set(nums[qs[i][0]-1:qs[i][1]]))))