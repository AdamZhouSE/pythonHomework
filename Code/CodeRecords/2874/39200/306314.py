n = int(input())
nums = input().split()
count = 0
flag = 0 #0: 任意 1: 健身 2: 编程
for x in nums:
    if x == "0":
        flag = 0
        count += 1
    elif x == "1":
        if flag == 2:
            flag = 0
            count += 1
        else:
            flag = 2
    elif x == "2":
        if flag == 1:
            flag = 0
            count += 1
        else:
            flag = 1
    elif x == "3":
        if flag == 1:
            flag = 2
        elif flag == 2:
            flag = 1
print(count)
