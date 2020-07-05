t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    inp.sort()
    if n % 2 == 1:
        print(inp[(n+1)//2-1])
    else:
        res = (inp[n//2-1]+inp[n//2+1-1])//2
        print(res)
