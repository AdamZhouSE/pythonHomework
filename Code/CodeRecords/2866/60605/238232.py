# 题目描述
# Bob喜欢一切甜的东西。他最喜欢的巧克力棒由几块组成，每一块可能有一个坚果，也可能没有。
# Bob 想把这些巧克力棒重新分成若干份，使得每一份恰好有一个坚果，并且分的时候不能从一块巧克力的中间掰开。
#
# 你的任务是计算有多少种分配方案。分割线位置不同即可视为不同的方案。注意，如果不分的话，所有的巧克力棒即为一份，这份巧克力仍需保证只有一个坚果。
#
# 输入描述
# 第一行输入巧克力的块数 n( 1 ≤ n ≤ 100)
# 第二行有 n 个数，第 i 个数表示第 i 块巧克力上是否有坚果，如果有坚果为 1，否则为 0.
# 输出描述
# 输出一个数表示方案数

def func():
    n = int(input())
    li = []
    x = input().strip().split(" ")
    sumLi = 0
    tot = 1
    for i in x:
        li.append(int(i))
        sumLi += int(i)
    if sumLi == 1: return 1
    pos1 = []
    for i in range(n):
        if li[i] == 1: pos1.append(i)
    for i in range(len(pos1) - 1):
        tot *= pos1[i+1]-pos1[i]
    return tot

print(func())
