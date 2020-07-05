t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    if n == 1:
        if a[0] == b[0]:
            print("YES")
        else:
            print("NO")
    else:
        needBreak = False
        count = 0
        for j in range(n):
            save = b[j]-a[j]
            if save > 0:
                for k in range(j, n):
                    if b[k] != a[k]:
                        a[k] += save
                        count += 1
                    else:
                        needBreak = True
                        break
                if needBreak:
                    break
        if a == b:
            print("YES")
        else:
            print("NO")
