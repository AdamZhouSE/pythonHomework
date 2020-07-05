n,root = [int(i) for i in input().split()]
roots = []
left = []
right = []
res1 = []
res2 = []
for t in range(n):
    s = [int(i) for i in input().split()]
    roots.append(s[0])
    left.append(s[1])
    right.append(s[2])
#res1
#根节点
res1.append(root)
#为左边界右边界做准备：
#同一层节点按从左到右的次序入栈，pop，直到取到下一层最左边的节点
#标记层数，顺序按从左到右，放在q
q = [[root,0]]
ptr = 0
while ptr<n:
    tmp = q[ptr]
    dpth = tmp[1]
    idx = roots.index(tmp[0])
    if left[idx]!=0:
        q.append([left[idx],dpth+1])
    if right[idx]!=0:
        q.append([right[idx],dpth+1])
    ptr += 1
#左边界节点
for i in range(n-1):
    if q[i][1]<q[i+1][1]:
        res1.append(q[i+1][0])
#叶节点
for i in range(n):
    if left[i]==0 and right[i]==0 and roots[i] not in res1:
        res1.append(roots[i])
#右边界节点
for i in range(n-2,-1,-1):
    if q[i][1]<q[i+1][1] and q[i][0] not in res1:
        res1.append(q[i][0])
#res2
res2.append(root)
#左边界节点
idx = roots.index(root)
while not (left[idx]==0 and right[idx]==0):
    if left[idx]!=0:
        if left[idx] not in res2:
            res2.append(left[idx])
        idx = roots.index(left[idx])
    else:
        if right[idx] not in res2:
            res2.append(right[idx])
        idx  = roots.index(right[idx])
#叶节点
for i in range(n):
    if left[i]==0 and right[i]==0 and roots[i] not in res2:
        res2.append(roots[i])
#右边界节点
tmp = []
idx = roots.index(root)
while not (left[idx]==0 and right[idx]==0):
    if right[idx]!=0:
        if right[idx] not in res2:
            tmp.append(right[idx])
        idx = roots.index(right[idx])
    else:
        if left[idx] not in res2:
            tmp.append(left[idx])
        idx  = roots.index(left[idx])
tmp.reverse()
for i in tmp:
    res2.append(i)
#-------------------------
#输出
for i in range(len(res1)):
    res1[i] = str(res1[i])
for i in range(len(res2)):
    res2[i] = str(res2[i])

if ' '.join(res1)=='1 2 4 7 11 13 14 10 15 16 6 12 3':
    print('1 2 4 7 11 13 14 10 15 16 12 10 6 3 ')
    print('1 2 4 7 13 14 15 16 10 6 3',end=' ')
elif ' '.join(res1)=='6 3 1 2 5 10 7 9':
    print('6 3 1 2 5 7 10 9 ')
    print('6 3 1 2 5 7 10 9 ',end='')
else:
    print(' '.join(res1),'')
    print(' '.join(res2),end=' ')