import copy


def main():
    matrix = eval(input())
    start = [len(matrix) - 1, 0]
    result = []
    for i in range(0, len(matrix) + len(matrix[0]) - 1):
        point = copy.deepcopy(start)
        point.append(matrix[point[0]][point[1]])
        array = []
        while point[0] < len(matrix) and point[1] < len(matrix[0]):
            temp = copy.deepcopy(point)
            array.append(temp)
            try:
                point[0] += 1
                point[1] += 1
                point[2] = matrix[point[0]][point[1]]
            except IndexError:
                break
        array = sorted(array, key=lambda x: x[2])
        array[0][0] = start[0]
        array[0][1] = start[1]
        for j in range(1, len(array)):
            try:
                array[j][0] = array[j - 1][0] + 1
                array[j][1] = array[j - 1][1] + 1
            except IndexError:
                break
        result.append(array)
        if start[0] != 0:
            start[0] -= 1
        else:
            start[1] += 1

    for i in range(0, len(result)):
        for j in range(0, len(result[i])):
            matrix[result[i][j][0]][result[i][j][1]] = result[i][j][2]

    print(matrix)


if __name__ == "__main__":
    main()
