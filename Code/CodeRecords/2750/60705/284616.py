# leetcode 310 最小高度树
import collections


def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]
    e = collections.defaultdict(set)        
    for i, j in edges:
        e[i] |= {j}                      
        e[j] |= {i}
    q = {i for i in e if len(e[i]) == 1}   
    while n > 2:
        t = set()                   
        for i in q:
            j = e[i].pop()          
            e[j] -= {i}      
            if len(e[j]) == 1:      
                t |= {j}
            n -= 1                
        q = t
    return list(q)


if __name__ == '__main__':
    n = int(input())
    edges = input()[2:-2].split("], [")
    for i in range(0, len(edges)):
        edges[i] = list(map(int, edges[i].split(",")))
    print(findMinHeightTrees(n, edges))

