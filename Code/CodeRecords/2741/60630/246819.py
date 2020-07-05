num = [int(p) for p in input("")[1 : -1].split(',')]

tmp = 1
ans = 1
for i in range(1, len(num)) :
    if num[i] > num[i-1] :
        tmp += 1
    else :
        tmp = 0
    if tmp > ans :
        ans = tmp

print(ans)
