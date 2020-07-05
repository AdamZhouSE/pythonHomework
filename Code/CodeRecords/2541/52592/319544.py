from collections import defaultdict
class F:
    def f(self, numCourses, prerequisites):
        
        graph = defaultdict(list)
        degree = [0] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        res = []
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        #print(bfs)
        for i in bfs:
            res.append(i)
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return res if len(res) == numCourses else []

q=int(input())
n=eval(input())

s=F()
res=s.f(q,n)
print(res)