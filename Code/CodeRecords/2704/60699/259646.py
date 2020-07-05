edges=input().split(',')
list1=[]
for i in range(0,len(edges),2):
    if i == 0:
        list1.append([(int)(edges[i][2]),(int)(edges[i+1][0])])
    else:
        list1.append([(int)(edges[i][2]), (int)(edges[i+1][0])])
edges=list1
p = [[i] for i in range(len(edges) + 1)]  # 并查集初始化
for x, y in edges:
    if p[x] is not p[y]:  # 如果两个集合地址不一样
        if len(p[x]) < len(p[y]):  # 权重优化判断
            x, y = y, x
        p[x].extend(p[y])  # 合并集合
        for z in p[y]:
            p[z] = p[x]  # 修改元素集合标记的指针地址
    else:
        print([x, y])
        break