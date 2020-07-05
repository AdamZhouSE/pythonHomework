num = int(input())
for i in range(num):
    p = m = int(input())
    n = list(map(int, input().split()))
    n.sort(reverse=True)
    for k in range(m):
        if n[m-k-1] >= p:
            print(p)
            break
        else:
            p = p-1
