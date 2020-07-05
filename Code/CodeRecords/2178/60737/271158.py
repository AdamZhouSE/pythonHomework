s = []
n = int(input())
nums = [int(i) for i in input().split( )]
while n:
    s.append(nums.pop(0))
    temp = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]
    ret = []
    for sub in temp:
        if sub not in ret:
            ret.append(sub)
    print(len(ret))
    n -= 1
    