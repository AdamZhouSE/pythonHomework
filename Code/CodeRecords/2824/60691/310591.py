s1 = list(map(int, input().split(' ')))
s2 = list(map(int, input().split(' ')))

length = s1[0]
limit = s1[1]
num = s1[2]

count = 0
for i in range(length-num+1):
    isproper = True
    for j in range(i, i+num):
        if s2[j] > limit:
            isproper = False
            break
        else:
            continue

    if isproper:
        count += 1

print(count)