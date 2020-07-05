list1 = input()[1:-1].split(",")
lower = int(input())
upper = int(input())
for i in range(len(list1)):
    list1[i] = int(list1[i])
count = 0
for j in range(len(list1)):
    for k in range(j + 1, len(list1) + 1):
        if lower <= sum(list1[j:k]) <= upper:
            count += 1
print(count)