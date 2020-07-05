num = input().split(",")
res = [0, 0]
m = len(num)
for i in range(len(num)):
    if num.count(num[i]) == 2:
        res[0] = int(num[i])
    if num.count(str(i+1)) == 0:
        res[1] = i + 1
print(res)