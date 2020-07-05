# 题目描述
# 给你一个由 n 个不同整数组成的序列 a。您可以将这个序列分成两个序列 b 和 c，这样每个元素都正好属于其中一个序列。
#
# 设 B 是属于 b 的元素之和，C 是属于 c 的元素之和（如果其中一些序列为空，则其和为0）。B - C 的最大可能值是多少？
#
# 输入描述
# 输入第一行为序列 a 的长度 n (1 ≤ n ≤ 100)
# 第二行为 n 个整数 ( - 100 ≤ ai ≤ 100) 表示 a 的每个元素
# 输出描述
# 根据题意输出 B - C 的最大值

n = int(input())
li = []
tmp = input().strip().split(" ")
for i in tmp:
    li.append(int(i))
s = sum(li)
b = 0
li = sorted(li, reverse=True)
for i in li:
    if i <= 0: break
    b += i

print(2*b-s)