T = int(input())
while T > 0:
    T -= 1
    N, x = input().split(' ')
    N = int(N)
    x = int(x)
    lst1 = []
    for i in range(0, N):
        nums = input().split(' ')
        for j in range(0, N):
            lst1.append(nums[j])
    lst2 = []
    for i in range(0, N):
        nums = input().split(' ')
        for j in range(0, N):
            lst2.append(nums[j])
    res = 0
    for i in range(0, len(lst1)):
        for j in range(0, len(lst2)):
            if int(lst1[i]) + int(lst2[j]) == x:
                res += 1
    print(res)
