length_limit = input().split(" ")
length = int(length_limit[0])
limit = int(length_limit[1])
list1 = input().split(" ")
list1 = [int(i) for i in list1]
count = 0

for i in range(length):
    if i < length - 1:
        if list1[i + 1] - list1[i] <= limit:
            count += 1
        else:
            count = 0
    else:
        count += 1
if limit == 0:
    count = 0
    print(" ".join(length_limit))
print(count)
