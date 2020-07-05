num = int(input())
bulb_list = []
for i in range(num):
    bulb_list.append(1)
if num > 1:
    for i in range(2, num + 1):
        for j in range(i - 1, num, i):
            if bulb_list[j] == 1:
                bulb_list[j] = 0
            else:
                bulb_list[j] = 1
    count = 0
    for i in bulb_list:
        if i == 1:
            count = count + 1
    print(count)
else:
    print(1)