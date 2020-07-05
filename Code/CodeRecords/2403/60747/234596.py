s=int(input())
peo=int(input())
count = 0
list1 = [0 for i in range(peo)]
while s > 0:
    for i in range(peo):
        count = count + 1
        if s < count:
            count = s
            list1[i] = list1[i] + count
            s = 0
            break
        else:
            s = s - count

        list1[i] = count + list1[i]
print(list1)

