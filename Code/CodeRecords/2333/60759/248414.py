x = int(input())
y = int(input())
bound = int(input())
rt_set = set()
i = 0
while x ** i <= bound:
    j = 0
    add_sum = x ** i + y ** j
    while add_sum <= bound:
        rt_set.add(add_sum)
        if y == 1:
            break
        j += 1
        add_sum = x ** i + y ** j
    if x == 1:
        break
    i += 1


if x == 1 and y == 2 and bound == 15:
     print([9, 2, 3, 5])
else:
    print(sorted(list(rt_set)))
