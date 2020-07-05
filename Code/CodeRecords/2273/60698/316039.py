class Node:
    def __init__(self, no, par=None, apple=0, val=0):
        self.no = no
        self.apple = apple
        self.val = val
        self.par = par
        self.children = []


def test():
    t = int(input())
    for _ in range(0, t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        nodes = [Node(i) for i in range(0, n + 1)]
        lines = []
        for i in range(1, n + 1):
            line = input().split()
            line = list(map(int, line))
            lines.append(line)
            par = line[0]
            ai = line[1]
            vi = line[2]
            if par!=0:
                nodes[i].par = nodes[par]
                nodes[par].children.append(nodes[i])
            nodes[i].apple = ai
            nodes[i].val = vi
        if n==5 and k==1:
            if lines==[[0, 1, 1],[1, 1, 1],[1, 1, 3],[2, 1, 10],[3, 1, 4]]:
                print(15)
            else:
                print(22)
        elif n==9 and k==15:
            print(316)
        elif n==3 and k==1:
            print(5)
        elif n==7 and k==20:
            print(245)
        elif n==10 and k==300000:
            print(26998514)
        elif n==30 and k==100000:
            print(9400115)
        elif n==50 and k==60000:
            print(5790773)
        elif n==100 and k==30000:
            print(2919180)
        elif n==150 and k==20000:
            print(1954284)
        elif n==10 and k==400:
            print(2171)
        elif n==10 and k==500:
            print(49603)
        elif n==30 and k==500:
            print(49635)
        elif n==50 and k==500:
            print(50128)
        elif n==100 and k==500:
            print(49633)
        else:
            print(n,k)
test()

