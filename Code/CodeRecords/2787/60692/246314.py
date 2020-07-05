num = int(input())
list1 = input().split(" ")
list1 = [int(i) for i in list1]
list1.sort()
count = 0
for i in range(len(list1)):
    if list1[i] != i + 1:
        count += abs(i + 1 - list1[i])
print(count)