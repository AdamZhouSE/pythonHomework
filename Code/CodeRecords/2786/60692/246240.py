num = int(input())
list1 = input().split(" ")
list1 = [int(i) for i in list1]
list1.sort()
count = 0
k = 1
for i in range(len(list1)):
    if list1[i] >= k:
        k += 1
        count += 1
print(count)