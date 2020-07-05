num = sorted(int(p) for p in input("")[1 : -1].split(','))
n = len(num)
res = []

cnt = 1
for i in range(1, n) :
    if num[i] != num[i-1] :
        if cnt > n / 3 :
            res.append(num[i-1])
        cnt = 1
    else :
        cnt += 1
if cnt > n / 3 :
   res.append(num[i-1])

print(res)
