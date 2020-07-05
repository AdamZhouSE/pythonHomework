test_num = int(input())
for i in range(test_num):
    s = input()
    sum_left = 0
    sum_right = 0
    for j in s:
        if j == "(":
            sum_left += 1
        else:
            sum_right += 1
    print(min(sum_left,sum_right)*2)