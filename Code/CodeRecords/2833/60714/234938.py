n = int(input())
volume = [int(x) for x in input().split()]
capacity = [int(x) for x in input().split()]
a = max(volume)
volume.remove(a)
b = max(volume)
if a + b > sum(volume):
    print("YES")
else:
    print("NO")
