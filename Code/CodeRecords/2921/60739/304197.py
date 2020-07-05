def isValid(matrix, n, m, d):
    base = matrix[0][0]
    for i in matrix:
        for j in i:
            if (j - base) % d != 0:
                return False
    return True

def getSum(matrix):
    total = 0
    for i in matrix:
        for j in i:
            total += j
    return total

def MatrixToList(matrix):
    l = []
    for i in matrix:
        for j in i:
            l.append(j)
    return l

def getOperator(matrix, n, m, d):
    if isValid(matrix, n, m, d):
        operator = 2000
        s = getSum(matrix)

        l = MatrixToList(matrix)
        for i in l:
            target = i
            tmp = 0
            for i in matrix:
                for j in i:
                    tmp += int(abs(target - j) / d)
            operator = min(tmp, operator)
        print(operator)
        return operator

    else:
        print(-1)
        return -1

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input_str = getInput()
n = input_str[0]
m = input_str[1]
d = input_str[2]

l = []
for i in range (n):
    l.append(getInput())

getOperator(l, n, m, d)