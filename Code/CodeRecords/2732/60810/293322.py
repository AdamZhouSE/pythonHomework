'''
很长一段时间以来，汤姆和杰里一直在争夺一块奶酪。所以最后你来营救，并决定战斗的结果将由一个数学游戏决定，其中你将写一个数字N。
汤姆和杰里将交替玩游戏，他们每个人都会减去数字n [n <N]，使得N％n = 0。 游戏被逐个重复进行，直到不能再进一步移动的那个游戏为止。
游戏以汤姆开始，众所周知，他们两个都将以最佳方式进行动作，您将确定谁赢得了比赛。
'''


def getRes(a, b, c):
    ans = 1
    t = a % c
    while b:
        if b & 1:
            ans = ans * t % c
        t = t * t % c
        b >>= 1
    print(ans)


t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    getRes(a, b, c)