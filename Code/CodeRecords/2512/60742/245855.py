n,p = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
m = int(input())
for t in range(m):
    inp = [int(i) for i in input().split()]
    if inp[0]==1:
        for i in range(inp[1],inp[2]+1):
            a[i-1] *= inp[3]
    elif inp[0]==2:
        for i in range(inp[1],inp[2]+1):
            a[i-1] += inp[3]
    else:
        sum = 0
        for i in range(inp[1],inp[2]+1):
            sum += a[i-1]
        sum %= p
        print(sum)