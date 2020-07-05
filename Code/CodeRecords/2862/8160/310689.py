n = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
arr.sort()
arr.reverse()

odd = []
even = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even1 = even.copy()
odd1 = odd.copy()

while True:
    if even1.__len__() > 0:
        del even1[0]
        if odd1.__len__() > 0:
            del odd1[0]
        else:
            break
    else:
        break
count1 = 0
for i in even1:
    count1 += i
for i in odd1:
    count1 += i
while True:
    if odd.__len__() > 0:
        del odd[0]
        if even.__len__() > 0:
            del even[0]
        else:
            break
    else:
        break
count2 = 0
for i in even:
    count2 += i
for i in odd:
    count2 += i
print(min(count1, count2))
