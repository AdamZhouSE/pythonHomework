# 题目描述
# 肖恩要把一个 m GB 的大文件保存到一个U盘上。
# 他有 n 个U盘，容量分别为 a1, a2, ..., an GB。
# 假设这个大文件可以被分成任意份存储，请帮助肖恩计算最少需要的U盘数量。
#
# 输入描述
# 第一行包含正整数 n（1 ≤ N ≤ 100）- U 盘的数量。
# 第二行包含正整数 m（1 ≤ M ≤ 10^5）- 文件的大小。
# 接下来的 n 行每行包含正整数 ai（1 ≤ ai ≤ 1000）U盘容量。
# 保证答案存在。
# 输出描述
# 输出一个整数表示最少需要的U盘数

n = int(input())
m = int(input())
storage = []
for i in range(n):
    storage.append(int(input()))

storage = sorted(storage, reverse=True)
cnt = 0
for i in storage:
    cnt += 1
    m -= i
    if m <= 0: break
print(cnt)