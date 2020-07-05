t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ');nums=[int(x) for x in nums]
    odd=[];even=[]
    for i in range(n):
        if nums[i]%2==1:
            odd.append(nums[i])
        else:
            even.append(nums[i])
    odd.sort();odd.reverse()
    even.sort();odd.extend(even)
    odd=[str(x) for x in odd]
    print(' '.join(odd)+' ')
