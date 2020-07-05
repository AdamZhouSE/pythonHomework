n = int(input())
list1 = input().split(" ")
list1 = [int(i) for i in list1]
count = 0
for i in list1:
    if i >= 0:
        count += abs(i - 1)
    else:
        if i != -1:
            count += abs(-1 - i)
        else:
            count += 1
print(count)