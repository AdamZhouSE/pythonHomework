# 建立数组，元素为三元组（str）
# 题目漏了条件：第一个三元组的第一个字母是根节点
def pre_order(a,str):
    root = str[0]
    if root=='*':
        return
    print(root,end='')
    if str[1]!='*':
        for pair in a:
            if str[1]==pair[0]:
                pre_order(a,pair)
    if str[2]!='*':
        for pair in a:
            if str[2]==pair[0]:
                pre_order(a,pair)        

n = int(input())
a = []
for i in range(n):
    a.append(input())
pre_order(a,a[0])