nums=list(map(int,input().split(',')))
t=int(input())
if t not in nums:
    nums.append(t)
    nums.sort()
    print(nums.index(t))
else:
    print(nums.index(t))