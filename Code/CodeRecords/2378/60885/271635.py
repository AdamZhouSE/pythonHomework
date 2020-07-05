def printM():
    print('='*n*3)
    for row in M:
        print(row)
    print('='*n*3)

def find_cycle_in(M,n,path):
    pre = path[-1]
    for j in range(n):
        if M[pre][j] != 0:
            if j == path[0] and len(path) > 2:
                return path + [j]
            if not j in path:
                cycle = find_cycle_in(M,n,path+[j])
                if cycle:
                    return cycle
    return None

def find_cycle(M,n):
    for i in range(n):
        cycle = find_cycle_in(M,n,[i])
        if cycle:
            return cycle
    return None

def single(M, i):
    count = 0
    for num in M[i]:
        if num != 0:
            count += 1
    return count <= 1

def find_max_edge(M, cycle):
    m = [0, 0, 0]
    for i in range(len(cycle)-1):
        j,k = cycle[i:i+2]
        temp = M[j][k]
        if temp > m[0]:
            m = [temp, j, k]
    return m

def delete_max_cycle(M,n):
    # printM()
    cycle = find_cycle(M,n)
    # print(cycle)
    # print()
    if not cycle:
        return 0
    ans = 0
    m,j,k = find_max_edge(M, cycle)

    m = M[j][k]
    M[j][k] = 0
    M[k][j] = 0

    temp = m + delete_max_cycle(M,n)
    if temp > ans:
        ans = temp
    
    M[j][k] = m
    M[k][j] = m

    return ans

n,k = list(map(int, input().split()))
M = [[0 for i in range(n)] for i in range(n)]
for i in range(k):
    i,j,m = list(map(int, input().split()))
    M[i-1][j-1] = m
    M[j-1][i-1] = m
result = delete_max_cycle(M,n)

print(result, end='')
