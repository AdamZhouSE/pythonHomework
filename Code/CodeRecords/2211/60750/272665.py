'''众所周知，皇室家族的名字非常有讲究。而作为研究皇室的历史学家的你，最近接到了一个艰巨的任务——分析王国历史中所有皇室夫人的名字。
王国历史上有n位皇室夫人，方便起见，我们将其从1至n编号。除了1号夫人外，其余夫人的名字均为一个大写字母连接着她母亲的名字。
而1号夫人作为王国的首任王后，她的名字只有一个大写字母。
例如，由于 AENERYS 由 A 与 ENERYS 组成，因此 ENERYS 是 AENERYS 的母亲。相似地，AENERYS 是 DAENERYS 与 YAENERYS 的母亲。
你知道王国历史上所有皇室夫人的姓名与关系，而你需要完成的任务是，对于其他历史学家感兴趣的名字串s，总共有多少位夫人的名字是以s起始的。
例如在样例的皇室族谱中，S 至 AENERYS 的这一支（包含 YS、RYS、ERYS、NERYS 与 ENERYS 这几位夫人）均只有一位女儿。接下来 AENERYS 有两位女儿，
分别是 DAENERYS，以及女儿是 RYAENERYS 的 YAENERYS。在这个皇室家族内，有两位夫人的名字以 RY 起始，她们是 RYS 与 RYAENERYS。
而 ERYS 与 ENERYS 均以 E 起始。名字以 N 起始的仅有一位夫人 NERYS。同样地，以 S 起始的仅有首位王后 S。而没有任何一位夫人的名字以 AY 起始。'''


def solve():
    line = input().split(' ')
    n = int(line[0])
    k = int(line[1])
    relation = []
    ladies = []
    for i in range(0,n):
        line2 = input().split(' ')
        relation.append(line2)
    for i in range(0,k):
        line3 = input()
        ladies.append(line3)

    names = []
    for i in range(0,n):
        mum = int(relation[i][1])
        if mum == 0:
            names.append(relation[i][0])
        else:
            names.append(relation[i][0] + names[mum - 1])

    res = []
    for i in range(0,k):
        tmp = 0
        for j in range(0,n):
            l = ladies[i]
            r = names[j]
            if ladies[i] in names[j]:
                if names[j].index(ladies[i]) == 0:
                    tmp += 1
        res.append(tmp)

    for i in range(0,k):
        print(res[i])

solve()


