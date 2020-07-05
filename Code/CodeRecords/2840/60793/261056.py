
temp = list(input().split(" "))
k, m = int(temp[0]), int(temp[1])
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
a.sort()
b.sort()
maxA = a[k-1]
minB = b[-m]
if maxA < minB:
    print("YES")
else:
    print("NO")