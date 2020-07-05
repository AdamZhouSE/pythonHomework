t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    nums = [int(n) for n in input().split( )]
    p = cmd[1]
    n = cmd[0]
    bool = False
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]*nums[j] == p:
                bool = True
    print('Yes' if bool else 'No')
    t -= 1
    