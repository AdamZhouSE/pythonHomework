# 拓扑排序
# 这个问题相当于查找一个循环是否存在于有向图中。
# 如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 用二维数组存图 判断有没有循环
# 有循环则失败
# https://www.jianshu.com/p/4565fa200a62
# 1.删除没有入度的节点
# 2.找环
import collections

numCourses = int(input())
eg="[[1,0],[2,0],[3,1],[3,2]]"
s=input()
s=s[1:len(s)-1]
for i in range(len(s)):
    if(s[i]==',' and s[i-1]==']'):
        s=s[:i]+'!'+s[i+1:]
s=s.split('!')
arr=[]
for i in s:
    arr.append(list(map(int,i[1:len(i)-1].split(','))))
res = []
indegree = [0 for _ in range(numCourses)]
adj = [set() for _ in range(numCourses)]
for sec, fir in arr:
    indegree[sec] += 1
    adj[fir].add(sec)
que=[]
for i in range(numCourses):
    if indegree[i] == 0:
        que.append(i)
while que:
    t = que.pop(0)
    res.append(t)
    for i in adj[t]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)
if len(res) == numCourses:
    print(res)
else:
    print([])
