n = int(input())
inp = [int(x) for x in input().split(" ")]
count = 0
# 记录前一天的情况
prefix = 0
for i in range(n):
    # 0或连续两天数字相同，休息
    if inp[i] == 0 or inp[i] == prefix and prefix != 3:
        count += 1
        prefix = 0
    # 3则取1，2中的一个数字（与前一个不同）
    elif inp[i] == 3:
        prefix = 3-prefix
    else:
        prefix = inp[i]
print(count)
