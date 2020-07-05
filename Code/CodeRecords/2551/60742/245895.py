n,m = [int(i) for i in input().split()]
a = [False]*n
for t in range(m):
    inp = [int(i) for i in input().split()]
    if inp[0]==0:
        for i in range(inp[1],inp[2]+1):
            a[i-1] = not a[i-1]
    else:
        sum = 0
        for i in range(inp[1],inp[2]+1):
            if a[i-1]:
                sum += 1
        print(sum)