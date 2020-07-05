list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
count = 0
if len(list1) % 2 == 0:
    mid = len(list1) / 2 - 1
else:
    mid = int(len(list1) // 2)
for i in list1:
    count += abs(i - list1[mid])
print(count)