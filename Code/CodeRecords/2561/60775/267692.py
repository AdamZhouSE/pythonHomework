


test = int(input())
for i in range(test):
    input1 = input().split(' ')
    N = int(input1[0])
    x = int(input1[1])
    matrix1 = []
    matrix2 = []
    count = 0
    for j in range(N):
        row = [int(tmp) for tmp in input().split(' ')]
        matrix1.extend(row)
    for j in range(N):
        row = [int(tmp) for tmp in input().split(' ')]
        matrix2.extend(row)
    for j in range(N*N):
        for k in range(N*N):
            if matrix1[j] + matrix2[k] == x:
                count += 1
print(count)