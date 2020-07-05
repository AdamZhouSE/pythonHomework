def find(x):
    if s[x] < 0:
        return x
    else:
        return find(s[x])
# 并查集
# 只需要给序号分类 在类别里分别进行排序
import re
string = list(input())
lst = list(map(int,re.findall(r'\d+',input())))
pairs = []

for i in range(len(lst)//2):
    pairs.append([lst[2*i], lst[2*i+1]])

s = [-1]*len(string)
# 合并
for pair in pairs:
    root1 = find(pair[0])
    root2 = find(pair[1])
    if root1 <= root2:
        s[root2] = root1
        s[root1] -= 1
    else:
        s[root1] = root2
        s[root2] -= 1

roots = []
for i in range(len(s)):
    if s[i]>=0:
        s[i] = find(i)
    else:
        roots.append(i)
for root in roots:
    index =[i for i in range(len(s)) if s[i] == root]
    index.append(root)
    index.sort()
    letters = [string[x] for x in index]
    letters.sort()
    for i in range(len(index)):
        string[index[i]] = letters[i]

print(''.join(string))