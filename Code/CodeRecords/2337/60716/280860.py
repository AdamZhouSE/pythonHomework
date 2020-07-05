#初步想法：通过能放炸弹的地点使用permutation来寻找满足炸弹互不炸到的最大可能值
n,m = map(int,input().split())
maps = list()
for i in range(n):
    strs = list(input())
    maps.append(strs)