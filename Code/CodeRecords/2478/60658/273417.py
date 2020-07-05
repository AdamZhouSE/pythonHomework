t = int(input())
for i in range(t):
    a,b = [int(x) for x in input().split()]
    k = int(input())
    delta = b-a
    ans = a+delta*(k-1)
    print(ans)