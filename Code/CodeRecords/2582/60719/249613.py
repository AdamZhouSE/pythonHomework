array1 = input().split(",")
array2 = input().split(",")
l1 = len(array1)
l2 = len(array2)
for i in range(l1):
    array1[i] = int(array1[i])
for j in range(l2):
    array2[j] = int(array2[j])
total = 0
for i in range(l1):
    for j in range(l2):
        total = max(total, abs(array1[i]-array1[j])+abs(array2[i]-array2[j])+abs(i-j))
print(total)