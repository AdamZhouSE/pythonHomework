T = int(input())
while T > 0:
    T -= 1
    length, n = input().split(' ')
    n = int(n)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    isExi = False
    for i in range(0, len(num) - 1):
        for j in range(i, len(num)):
            if num[i]*num[j]==n:
                isExi = True
                break
    if isExi:
        print("Yes")
    else:
        print("No")
