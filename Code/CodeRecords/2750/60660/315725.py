from collections import defaultdict

def findMinHeightTrees( n, edges):
    if n <= 2:
        return [i for i in range(n)]
    in_degrees = [0] * n
    res = [True] * n
    adjs = defaultdict(list)
    for edge in edges:
        in_degrees[edge[0]] += 1
        in_degrees[edge[1]] += 1
        adjs[edge[0]].append(edge[1])
        adjs[edge[1]].append(edge[0])
    from collections import deque
    deque = deque()

    for i in range(n):
        if in_degrees[i] == 1:
            deque.append(i)
    while n > 2:
        size = len(deque)
        n -= size
        for i in range(size):
            top = deque.popleft()
            res[top] = False

            successors = adjs[top]
            successors.append(top)

            for item in successors:
                in_degrees[item] -= 1

                if in_degrees[item] == 1:
                    deque.append(item)

    return [i for i in range(len(res)) if res[i]]

n=int(input())
l=eval(input())
print(findMinHeightTrees(n,l))