tests = list(map(int,input().split()))
nums = list(map(int,input().split()))
for i in range(0,tests[1]):
    ls = list(map(int,input().split()))
    if ls[0]==1:
        start = ls[1]
        end = ls[2]
        tem = ls[3]
        k = ls[4]
        for i in range(start-1,end):
            nums[i]+=tem
            tem+=k
    else:
        print(nums[ls[1]-1])