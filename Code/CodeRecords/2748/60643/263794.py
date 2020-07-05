def isvalid(string:str):  # 判断括号串是否合法
    l_minus_r = 0
    for c in string:
        if c == '(':
            l_minus_r += 1
        elif c == ')':
            l_minus_r -= 1
            if l_minus_r < 0:# 只用中途出现了负值，你就要终止循环，已经出现非法字符了
                return False
    return l_minus_r == 0

s=input()
level = {s}#一开始就是输入的str
valid=[]
# BFS
while not valid:#还未得到结果时一直循环
    valid = list(filter(isvalid, level))#所有左右括号数目相等的合法组合
    if valid:
        print(valid)#当前valid不为空，说明已经有合法字符串产生了
    nextLevel=set()
    for item in level:
        for i in range(len(item)):
            if item[i] in "()":
                nextLevel.add(item[:i]+item[i+1:])
    level=nextLevel
