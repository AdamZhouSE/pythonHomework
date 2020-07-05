left = int(input())
right = int(input())
res = []
for num in range(left, right + 1):
    if '0' in str(num):
        continue
    for n in str(num):
        if num % int(n) != 0:
            break
    else:
        res.append(num)
print(res)