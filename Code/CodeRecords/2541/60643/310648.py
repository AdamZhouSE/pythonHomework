def solution( prerequisites,numCourses):
    # 课程的长度
    clen = len(prerequisites)
    if clen == 0:
        return []
    # 入度数组
    in_degrees = [0 for _ in range(numCourses)]
    # 邻接表
    adj = [set() for _ in range(numCourses)]
    # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
    # 1 -> 0，这里要注意：不要弄反了
    for second, first in prerequisites:
        in_degrees[second] += 1
        adj[first].add(second)

    # print("in_degrees", in_degrees)
    # 首先遍历一遍，把所有入度为 0 的结点加入队列
    res = []
    queue = []
    for i in range(numCourses):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        top = queue.pop(0)
        res.append(top)

        for successor in adj[top]:
            in_degrees[successor] -= 1
            if in_degrees[successor] == 0:
                queue.append(successor)
    if len(res) != numCourses:
        return []
    return res

if __name__=="__main__":
    n=int(input())
    lsn=eval(input())
    for item in lsn:
        item=list(reversed(item))
    lsn=sorted(lsn)
    ans=solution(lsn,n)
    print(ans)