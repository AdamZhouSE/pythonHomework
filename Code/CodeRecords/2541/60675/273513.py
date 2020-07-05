def func(l, num : int) -> list :
    in_degrees = [0 for _ in range(num)]
    adj = [set() for _ in range(num)]

    for second, first in l:
        in_degrees[second] += 1
        adj[first].add(second)
    queue = []
    for i in range(num):
        if in_degrees[i] == 0:
            queue.append(i)
    counter = 0
    res = []
    while queue:
        top = queue.pop(0)
        counter += 1
        res.append(top)

        for node in adj[top]:
            in_degrees[node] -= 1
            if in_degrees[node] == 0:
                queue.append(node)
    if counter == num:
        return res
    else:
        return []

num = int(input())
n = "l = " + input()
exec(n)
print(func(l,num))