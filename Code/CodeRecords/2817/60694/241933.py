n = int(input())

l = list(map(int, input().split()))
l.insert(0, 0)

for i in range(1, n+1):
    a = l[i]
    b = l[a]
    c = l[b]
    if a == l[c]:
        print("YES")
        exit()
print("NO")
