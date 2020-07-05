n = int(input(""))
numbers = input("").split(' ')

cnt = 0
stat = 0
for i in range(0, n) :
    now = int(numbers[i])
    if now == 4 or now == 2:
        cnt += now >> 1
    elif now == 3:
        if stat < 0 :
            cnt += 2
        stat += 1
    else :
        if stat > 0 :
            cnt += 2
        stat -= 1

if stat > 0 :
    cnt = ((cnt + 1) >> 1) + stat
else :
    cnt = (cnt + ((-stat + 1) >> 1) + 1) >> 1

print(cnt)
