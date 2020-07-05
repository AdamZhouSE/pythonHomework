length_limit = input().split(" ")
length = int(length_limit[0])
limit = int(length_limit[1])
list1 = input().split(" ")
list1 = [int(i) for i in list1]
count = 1
for i in range(1, length):
    if list1[i] - list1[i - 1] > limit:
        count = 0
    count += 1
if length == 1:
    count = 0
print(min(count, length))