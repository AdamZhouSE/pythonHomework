import collections
def removeStones(stones):
    m = 0                                    # 记录最大的行坐标
    row = collections.defaultdict(set)       # 记录每一行中点的列坐标
    col = collections.defaultdict(set)       # 记录每一列中点的行坐标

    for i,j in stones:                       # 遍历所有石头坐标
        row[i] |= {j}                        # 记录行对应的列坐标
        col[j] |= {i}                        # 记录列对应的坐标
        m = max(m,i)                         # 记录最大的行坐标


    graph = 0                                # 连通分量的个数

    for i in range(m+1):                     # 对于所有的i进行遍历
        if i in row:                         # 如果i在row中，即i对一个新的连通分量
            graph += 1                       # 连通分量数 +1
            stack = {i}                      # 这里用set模拟栈，方便后面合并操作

            while stack:                     # 栈非空时
                x = stack.pop()              # 从栈中不断弹出行坐标x
                for j in row[x]:             # 对于row[x]中所保存的所有列坐标j
                    if j in col:             # 如果col[j]非空，说明该列有对应的行
                                                 # 可以和当前行x构成连通分量
                        stack |= col[j]      # 将col[j]中所有的行合并到栈中
                        del col[j]           # 并删除col[j]，防止循环调用
                    
                del row[x]                   # 最后删除row[x]，防止循环调用

    return len(stones) - graph               # 针对于每个连通分量，最后只剩一个石子
                                                 # 因此剩余石子个数为连通分量个数graph
                                                 # 由于石子坐标是唯一的
                                                 # 因此总石子个数为stones的长度
                                                 # 可操作数为总石子数 - 剩余石子数
                                                 # 即 len(stones) - graph


if __name__ == "__main__":    
    stones=input().strip('[]').split("],[")
    stones=[i.split(",") for i in stones]
    l=len(stones)
    #print(stones)
    for i in range(l):
        for j in range(len(stones[0])):
            stones[i][j]=int(stones[i][j])
    #print(stones)
    x=removeStones(stones)
    
    print(x)