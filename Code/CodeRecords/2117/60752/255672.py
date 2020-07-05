num = int(input())
all = 0
for i in range(1, num + 1):
    ii = i
    count = 0

    for j in range(2, i+1):

        while ii % j == 0:
            ii = ii / j
            count += 1
            if ii == 0: break
        if ii == 0: break
    if count % 2 == 0:
        all += 1
print(all)
