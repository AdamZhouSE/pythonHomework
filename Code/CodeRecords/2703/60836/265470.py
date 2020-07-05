"""
班上有 N 名学生。其中有些人是朋友，有些则不是
他们的友谊具有是传递性: 如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友
所谓的朋友圈，是指所有朋友的集合
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系
如果 M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道
你必须输出所有学生中的已知的朋友圈总数
"""

def isin(i,m):
    for ch in i:
        if ch in m:
            return True
    return False


arr=eval(input())

friend_group=[]
for i in range(len(arr)):
    a=[]
    for m in range(len(arr[i])):
        if arr[i][m]==1:
            a.append(m)
    friend_group.append(a)

i=0
while i < len(friend_group):
    m=1+i
    while m<len(friend_group):
        if isin(friend_group[i],friend_group[m]):
            del friend_group[m]
        else:
            m+=1
    i+=1

print(len(friend_group))