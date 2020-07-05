n = int(input())

t = n
res = ""
while t != 0:
    remain = t % -2
    t //= -2
    if remain < 0:
        t += 1
        remain += 2
    res = res + str(remain)
print(res[::-1])