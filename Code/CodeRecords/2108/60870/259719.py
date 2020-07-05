num = input()
res = 0
for i in range(int(num) + 1):
    i = str(i)
    for ch in i:
        if ch == '1':
            res = res + 1
print(res)