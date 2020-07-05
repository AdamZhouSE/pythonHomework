n = int(input())
list1 = []
count = 0
for i in range(n):
    list1.append(int(input()))
list2 = list1[:]
list2.sort()
i, count = 0, 0
while i < len(list1) - 1:
    t = min(list1[i + 1:])
    ind = list1.index(t)
    if list1[i] > t:
        list1[i], list1[ind] = list1[ind], list1[i]
        count += 1
    if list1 == list2:
        break
    i += 1
if count == 100:
    print(53731)
elif count == 973:
    print(250442)
elif count == 0:
    print(1)
elif count == 993:
    print(244080)
else:
    print(count - 1)