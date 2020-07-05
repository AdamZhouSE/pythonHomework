t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    nums = input().split( )
    n = cmd[0]
    k = cmd[1]
    newnum = []
    times = (n-1)//k
    for i in range(times):
        temp = nums[i*k:i*k+k]
        temp.reverse()
        for num in temp:
            newnum.append(num)
    temp = nums[k*times:]
    temp.reverse()
    for num in temp:
        newnum.append(num)
    for item in newnum:
        print('{} '.format(item), end="")
    t -= 1
    print()
    