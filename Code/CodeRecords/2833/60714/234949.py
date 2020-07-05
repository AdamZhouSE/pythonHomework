n = int(input())
volume = [int(x) for x in input().split()]
capacity = [int(x) for x in input().split()]
a = max(capacity)
capacity.remove(a)
b = max(capacity)
if a + b >= sum(volume):
    print("YES")
else:
    print("NO")
