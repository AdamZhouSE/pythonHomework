inp = int(input())
res = 1
while True:
    if res * res > inp:
        res -= 1
        break
    res += 1
print(res)
