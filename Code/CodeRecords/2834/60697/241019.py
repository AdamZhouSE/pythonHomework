# 2 4
# # ABCD
# # ABCE
# # 1 2 3 4
sizes=list(map(int,input().split(' ')))
size=sizes[0]
title=sizes[1]
strs=[]
for i in range(size):
    strs.append(input())
grade=list(map(int,input().split(' ')))
res=0
maxindex=0
maxnum=0
for i in range(title):
    tmp = [0 for i in range(5)]
    for j in range(size):
        tmp[ord(strs[j][i])-65]=tmp[ord(strs[j][i])-65]+1
    maxnum=max(tmp)
    res=res+grade[i]*maxnum
print(res)

