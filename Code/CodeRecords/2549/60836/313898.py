"""
GY君购买了一批宝石放进了仓库。有一天GY君心血来潮，想要清点他的宝石，于是把m个宝石都取出来放进了宝石管理系统
每个宝石i都有一个珍贵值vi，他希望你能编写程序查找到从大到小第n珍贵的宝石
但是现在问题来了，他非常不小心的留了一些宝石在仓库里面，有可能要往现有的系统中添加宝石
这些宝石的个数比较少。他表示非常抱歉，但是还是希望你的系统能起作用
5 3
1 3 2 5 6
1 3
2 4
1 6
"""

s=[int(m) for m in str(input()).split(" ")]
N=s[0]
instr=s[1]

value=[int(m) for m in str(input()).split(" ")]
instruction=[]
for i in range(instr):
    instruction.append([int(m) for m in str(input()).split(" ")])

for i in range(len(instruction)):
    if(instruction[i][0]==1):
        value.sort()
        print(value[len(value)-instruction[i][1]])
    else:
        value.append(instruction[i][1])
