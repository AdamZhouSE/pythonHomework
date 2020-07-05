import collections

n=int(input())
edges=list(eval(input()))
if n == 1:
    print([0])
else:
    e = collections.defaultdict(set)        #字典初始化为集合
    for i, j in edges:
        e[i] |= {j}                         #把边哈希化，方便调用
        e[j] |= {i}
    q = {i for i in e if len(e[i]) == 1}    #建立初始宽搜队列，长度为1时代表只连接一个点
    while n > 2:
        t = set()                   #临时队列
        for i in q:
            j = e[i].pop()          #把连接点取出
            e[j] -= {i}             #连接是双向的，所以要删除关系
            if len(e[j]) == 1:      #更新后，如果长度为1时则加入下一个轮队列
                t |= {j}
            n -= 1                  #删除计数
        q = t
    print(list(q))