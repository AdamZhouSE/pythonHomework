n = eval(input())
m = eval(input())
res = 0
for x in n:
    cnt = 0
    if x in m:
        index = n.index(x)
        for y in range(m.index(x),len(m)):
            if index == len(n):
                break
            else:
                if m[y] != n[index]:
                    break
                else:
                    cnt = cnt + 1
                    index = index + 1
        if cnt > res:
            res = cnt
print(res)