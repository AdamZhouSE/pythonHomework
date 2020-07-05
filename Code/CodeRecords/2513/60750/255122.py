def solve():
    n = int(input())
    matrix = []
    for i in range(0,n):
        line = list(map(int,input().split(',')))
        matrix = matrix + line
    matrix.sort()
    k = int(input())
    print(matrix[k - 1])
    
solve()