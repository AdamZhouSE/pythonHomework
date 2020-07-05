# 题目描述
# b 序列有 n 个整数 b[1], b[2], ... b[n]，定义 a[i] = b[i] - b[i+1] + b[i+2] - ... b[n]。
#
# 现给定 a[1] 到 a[n] 的值，你能还原出 b 序列吗？
#
# 输入描述
# 第一行为序列的长度 n (2 ≤ n ≤ 100000)
# 第二行为 n 个数表示 a[i] (-10^9 ≤ a[i] ≤ 10^9)
# 输出描述
# 输出 b 序列，两两间用空格隔开

n = int(input())
t = input().strip().split(" ")
b = []
for i in t:
    b.append(int(i))
b.append(0)
a = []
for i in range(n):
    a.append(b[i] + b[i+1])

res = ""
for i in a:
    res = res + str(i) + " "
print(res.strip())