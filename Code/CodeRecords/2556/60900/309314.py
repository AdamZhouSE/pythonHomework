s1 =input().split(' ')
n =int(s1[0])
k =int(s1[1])
nums =[]
for i in range(0,n):
    nums.append(input().split(' '))
    nums[i][0] =int(nums[i][0])
    nums[i][1] = int(nums[i][1])
result =[]
for i in range(0,n-1):
    for j in range(i+1,n):
        c1 = abs(nums[i][0]-nums[j][0])
        c2 =abs(nums[i][1]-nums[j][1])
        if c1<k and c2<k:
            result.append((k-c1)*(k-c2))

if len(result)==1:
    print(result[0])
elif len(result)==0:
    print(0)
else:
    print(-1)