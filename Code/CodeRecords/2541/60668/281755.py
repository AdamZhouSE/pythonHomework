def find_20_lessons(n,prereq=[]):
    clen = len(prereq)
    if clen == 0:
        return  [i for i in range(n)]
    in_degree = [0 for _ in range(n)]
    adj = [set() for _ in range(n)]
    for second, first in prereq:
        in_degree[second] += 1
        adj[first].add(second)
    queue = []
    re = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        top = queue.pop(0)
        re.append(top)
        for suc in adj[top]:
            in_degree[suc]-=1
            if in_degree[suc] ==0:
                queue.append(suc)
    if len(re) != n:
        return []
    return re
if __name__=='__main__':
    n = int(input())
    prereq= eval(input())
    print(find_20_lessons(n,prereq))

   