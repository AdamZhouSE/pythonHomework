# 题目描述
# 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
#
# 返回 N 的长度。如果不存在这样的 N，就返回 -1。

n = int(input())
string = ""
isOK = False
for n in range(1, n+1):
    string = string + "1"
    if int(string)%n == 0:
        isOK = True
        print(string)
        break
if not isOK:
    print("-1")