n = int(input())
l = list(map(int, input().split()))
d = int(input())
res = []
for i in range(2**(d-1), 2**d):
    if 2**(d-1) > len(l):
        print("EMPTY")
        exit()
    if i <= len(l):
        res.append(l[i-1])
    else:
        break
print(*res)
