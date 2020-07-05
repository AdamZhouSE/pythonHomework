def getSequence(matrix):
    Sequence = []
    flag = -1

    while flag != 0:
        flag = 0

        for i in range (len(matrix)):
            if i not in Sequence:
                if isValid(matrix[i], Sequence):
                    Sequence.append(i)
                    flag += 1
    if len(Sequence) != len(matrix):
        return False
    return Sequence


def isValid(l, CurrentSequence):
    for i in range(len(CurrentSequence)):
        l[CurrentSequence[i]] = 0
    for i in l:
        if i == 1:
            return False
    return True

k = int(input())
point_list = eval(input())
matrix = []

for i in range (k):
    list = []
    for j in range(k):
        list.append(0)
    matrix.append(list)

for i in range (len(point_list)):
    x,y = point_list[i]
    matrix[x][y] = 1

# print(matrix)

print(getSequence(matrix))