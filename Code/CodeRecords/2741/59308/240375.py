a = eval(input())
temp = 1
res = 1
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        temp += 1
    else:
        res = max(res, temp)
        temp = 1
print(res)


