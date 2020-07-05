n = int(input())
res = False
for i in range(int(n ** 0.5) + 1):
    for j in range(int(n ** 0.5) + 1):
        if i ** 2 + j ** 2 == n:
            res = True
            break
    if res:
        break
print(res)