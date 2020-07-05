n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(n-1, -1, -1):
    if not a[i] in l:
        l.insert(0,a[i])
        
print(len(l))
print(*map(int, l))