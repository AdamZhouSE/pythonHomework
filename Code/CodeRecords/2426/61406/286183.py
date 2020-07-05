T = int(input())
for a in range(0,T):
    N = int(input())
    source = [int(x) for x in input().split()]
    result = 1
    for b in range(0,3):
        maxnum = max(source)
        result = result*maxnum
        source.remove(maxnum)
    print(result)