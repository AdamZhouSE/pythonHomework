import ast
import queue

def solve():
    n = int(input())
    nums = ast.literal_eval(input())
    res = []
    indegrees = [0 for i in range(n)]
    for i in range(0,len(nums)):
        indegrees[nums[i][0]] += 1

    q = queue.Queue()
    for i in range(n):
        if indegrees[i] == 0:
            q.put(i)

    while not q.empty():
        index = q.get()
        res.append(index)
        n -= 1
        for i in range(0,len(nums)):
            if nums[i][1] == index:
                if indegrees[nums[i][0]] - 1 == 0:
                    q.put(nums[i][0])
                indegrees[nums[i][0]] -= 1

    print(res)

solve()

