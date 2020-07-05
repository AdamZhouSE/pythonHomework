n = int(input())
a = [int(x) for x in input().split()]
k = 0
m = set()
 
for x in a:
    while(x in m):
        x += 1
        k += 1
    m.add(x)
print(k)