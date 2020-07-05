T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    rev = 0
    for j in range(N):
        for k in range(j+1,N):
            if nums[j]>nums[k]:
                rev += 1
    print(rev)
