def solve(A, F, res, ptr):
    if res[ptr] >= 0:
        return
    stack = [ptr]
    while stack:
        if res[stack[-1]] == -2:
            res[stack[-1]] = -1
            stack.append(F[stack[-1]])
        elif res[stack[-1]] == -1:
            last = stack.pop()
            ptr = stack.index(last)
            SUM = 0
            for i in stack[ptr:]:
                SUM += A[i]
            for i in stack[ptr:]:
                res[i] = SUM
            stack = stack[0:ptr + 1]  # cao 记得+1
        else:
            SUM = res[stack.pop()]
            if stack:
                res[stack[-1]] = SUM + A[stack[-1]]


N = int(input())
A = [int(i) for i in input().strip('[|]').split(' ')]
F = [(int(i) - 1) for i in input().strip('[|]').split(' ')]  # 已经减一
res = [-2] * N  # -2 表示未访问到 -1 表示在栈中 其余表示已完成
[solve(A, F, res, i) for i in range(N)]
[print(i) for i in res]
