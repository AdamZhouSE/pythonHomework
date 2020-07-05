t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    nums = [int(n) for n in input().split( )]
    s = cmd[1]
    l = cmd[0]
    ret = []
    for i in range(l-1):
        for j in range(i+1, l+1):
            if sum(nums[i:j]) == s:
                ret.append(str(i+1)+' '+str(j))
    if ret:
        print(ret[0])
    else:
        print(-1)
    t -= 1
    