# 题目描述
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
# 如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。
# 所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
# 如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，
# 否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

liofset = []
lioffriends = eval(input())
for i in range(len(lioffriends)):
    for j in range(len(lioffriends)):
        if lioffriends[i][j]==1:
            isIn = False
            for k in liofset:
                if i in k:
                    k.add(j)
                    isIn = True
                if j in k:
                    k.add(i)
                    isIn = True
            if isIn: break
            else:
                s = {i, j}
                liofset.append(s)
print(len(liofset))
