"""
小丑海盗船
读取一行n个数字，分别从左右两边向内，如果<=k，则去除该数字，否则停止比较
"""
line1 = input().split(" ")
line2 = input().split(" ")
n = int(line1[0])
k = int(line1[1])
count_left = 0
count_right = 0
# 分别从左右两边判断，如果体重大于k，则后面的孩子也不会被甩出去，break停止比较
for weight in line2:
    if int(weight) <= k:
        count_left += 1
    else:
        break
for i in range(0, n):
    # 这里用python特性，-1是最后一个元素，-2，-3等依次向前
    if int(line2[-i-1]) <= k:
        count_right += 1
    else:
        break
result = count_left + count_right
if result > n:
    result = n
print(result)
