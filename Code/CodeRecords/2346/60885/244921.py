def spiralStr(matrix):
    result = []
    while len(matrix) > 1:
        result.extend(matrix.pop(0))
        for i in range(len(matrix)-1):
            result.append(matrix[i].pop(-1))
        result.extend(matrix.pop(-1)[::-1])
        for i in range(len(matrix)):
            result.append(matrix[-1-i].pop(0))
    if len(matrix) > 0:
        result.extend(matrix[0])
    return result

def test():
    M,N = list(map(int, input().split()))
    nums = input().split()
    matrix = []
    for i in range(0,M*N,N):
        matrix.append(nums[i:i+N])
    result.append(spiralStr(matrix))

result = []
for i in range(int(input())):
    test()

for i in result:
    print(' '.join(i), end=' \n')
