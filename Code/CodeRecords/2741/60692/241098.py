list1 = input()[1:-1].split(",")
max_l = 1
this_l = 1
for i in range(1, len(list1)):
    if list1[i - 1] < list1[i]:
        this_l += 1
    else:
        max_l = max(max_l, this_l)
        this_l = 1
print(max_l)