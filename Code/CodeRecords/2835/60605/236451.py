# 题目描述
# Jeff 得到了 n 张纸牌，每张纸牌的数字要么是数字 0，要么是数字 5。
# Jeff 可以选择多张纸牌，并将它们排成一行，以得到某个数。
# 请问，Jeff 可以从纸牌得到的数中，能够被 90 整除的最大数是多少？
#
# Jeff 必须组成不含前导 0 的数。为此，我们还假定数 0 不含任何的前导 0。Jeff 不必使用所有的纸牌。
#
# 输入描述
# 第一行为纸牌数 n (1 ≤ n ≤ 10^3)。
# 接下来的一行包含了 n 个整数 (ai = 0 或 ai = 5). 数 ai 表示第 i 张纸牌上写的数字。
# 输出描述
# 如果能够组成被 90 整除的最大整数，输出这个数，否则输出 -1

n = int(input())
t = input().strip().split(" ")
li0 = 0
li5 = 0
for i in t:
    if i == "0": li0+=1
    if i == "5": li5+=1

is9 = False
cnt9 = 0
is10 = li0 > 0

div9 = li5 // 9
if div9 > 0:
    is9 = True
    cnt9 = div9*9

if is9 and is10:
    for i in range(cnt9): print("5", end="")
    for i in range(li0): print("0", end="")
    print()
elif is9 and not is10:
    print("-1")
elif not is9 and is10:
    print("0")
else:
    print("-1")