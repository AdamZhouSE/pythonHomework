t_num = input()
g_num = input().split(" ")
num_four = g_num.count('4')
num_three = g_num.count('3')
num_two = g_num.count('2')
num_one = g_num.count('1')
count = 0
count += num_four
if num_three >= num_one:
    count += num_one
    num_three = num_three - num_one
    count += num_three
    count = count + num_two//2
    num_two = num_two % 2
    count += num_two
else:
    count += num_three
    num_one = num_one - num_three
    if num_two % 2 == 0:
        count += num_two//2
        count += num_one//4
        num_one = num_one % 4
        if num_one != 0:
            count += 1
    else:
        count += (num_two+1) // 2
        if num_one > 2:
            num_one -= 2
            if num_one % 4 == 0:
                count += num_one//4
            else:
                count = count + num_one//4 + 1

print(count)