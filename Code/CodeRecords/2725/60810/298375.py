'''
很长一段时间以来，汤姆和杰里一直在争夺一块奶酪。所以最后你来营救，并决定战斗的结果将由一个数学游戏决定，其中你将写一个数字N。
汤姆和杰里将交替玩游戏，他们每个人都会减去数字n [n <N]，使得N％n = 0。 游戏被逐个重复进行，直到不能再进一步移动的那个游戏为止。
游戏以汤姆开始，众所周知，他们两个都将以最佳方式进行动作，您将确定谁赢得了比赛。
'''


def getMove(N):
    ret = []
    for i in range(1, N + 1):
        if (N - i) % i == 0:
            ret.append(i)
    return ret


def getBest(lis):
    ret = 0
    for m in lis:
        if not getMove(m):
            ret = m
            return ret
    for m in lis:
        if m > ret:
            ret = m
    return ret


def game(n):
    count = 0
    while n > 1:
        lis = getMove(n)
        if lis:
            move = getBest(lis)
            n -= move
            count += 1
        else:
            break
    if count % 2 == 1:
        print(0)
    else:
        print(1)


t = int(input())
for i in range(t):
    n = int(input())
    game(n)
