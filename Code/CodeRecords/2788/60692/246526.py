n = int(input())
list_1 = input().split(" ")
list_1 = [int(i) for i in list_1]
m = int(input())
list_2 = input().split(" ")
list_2 = [int(j) for j in list_2]
list_1.sort()
list_2.sort()
count = 0
j = 0
i = 0
for i in range(len(list_1)):
    while j < m:
        if abs(list_1[i] - list_2[j]) <= 1:
            j += 1
            count += 1
            break
        else:
            break
print(count)