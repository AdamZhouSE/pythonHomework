a = [int(i) for i in input().split(" ")]
n = a[0]
d = a[1]
m = int(input())
# y = -x+2n-d
for i in range(m):
    b = [int(i) for i in input().split(" ")]
    x = b[0]
    y = b[1]
    if(x==0):
        if(y==d):
            print("YES")
        else:print("NO")
        continue
    if (x == d and y <= 2 * d):
        print("YES")
        continue
    if (y / (x - d) >= 1 or y / (x - d) <= -1) and (y - d) / x <= 1 and (y - d) / x >= -1 and x + y <= (2 * n - d):
        print("YES")
    else:
        print("NO")
