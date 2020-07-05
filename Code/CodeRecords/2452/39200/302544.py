n = int(input())
M = []
for i in range(0, n):
    M.append(input().split(","))
target = int(input())

def cal(M, target):
    m = (n - 1) // 2
    start = 0
    end = n - 1
    while int(M[m][0]) >= target or int(M[m+1][0]) <= target:
        temp = m
        if int(M[m][0]) > target:
            m = (start + m) // 2
            end = temp
        else:
            m = (m + end) // 2
            start = temp
    return m
print(str(target) in M[cal(M, target)])
