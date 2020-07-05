w = [int(k) for k in input("")[1 : -1].split(',')]
m = int(input(""))

for i in range(max(w), max(w) * len(w)) :
    cnt = 0
    tmp = 0
    j = 0
    while j < len(w) :
        tmp += w[j]
        if tmp > i :
            cnt += 1
            tmp = w[j]
        j += 1
    if tmp > 0 :
        cnt += 1
    if cnt <= m :
        print(i)
        break