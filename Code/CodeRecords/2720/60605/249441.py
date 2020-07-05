# 题目描述
# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。
# 线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
#
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
#
# 给你这个计算机网络的初始布线 connections，
# 你可以拔开任意两台直连计算机之间的线缆，
# 并用它连接一对未直连的计算机。
# 请你计算并返回使所有计算机都连通所需的最少操作次数。
# 如果不可能，则返回 -1 。

def union(li, set1, set2):
    if set1 == set2: return 
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

n = int(input())
listOfConns = list(eval(input()))
linkages = len(listOfConns)
li = [-1 for i in range(n)]

for i in listOfConns:
    union(li, find(li, i[0]), find(li, i[1]))
# print(li)
minVal = -1
for i in li:
    minVal = min(minVal, i)
maxLinkage = -minVal
outspace = n-maxLinkage
useableLink = linkages-maxLinkage+1
if outspace <= useableLink:
    print(outspace)
else:
    print(-1)


