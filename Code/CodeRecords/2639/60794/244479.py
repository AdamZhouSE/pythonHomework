a = input()
b = int(input())
p = list(a)
ans = 0
for i in range(len(p)):
    x = b
    t = 0
    f = p[i]
    for j in range(i+1, len(p)):
        g = p[j]
        if g == f:
            if ans < j - i + 1:
                ans = j - i + 1
            continue
        else:
            if x > 0:
                if ans < j - i + 1:
                    ans = j - i + 1
                x = x - 1
            else:
                break
print(ans)