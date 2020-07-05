def s17():
    num = int(input())
    matrix = []
    for i in range(num):
        li = list(eval(input()))
        matrix.append(li)

    target = int(input())
    for i in range(num-1):
        if target < matrix[i][0]:
            if i == 0:
                print("False")
                return
            for j in range(len(matrix[i-1])):
                if target == matrix[i-1][j]:
                    print("True")
                    return
                if j == len(matrix[i-1]) - 1:
                    print("False")
                    return
    if target > matrix[num-1][len(matrix[num-1])-1]:
        print("False")
        return
    for j in range(len(matrix[num-1])):
        if target == matrix[num-1][j]:
            print("True")
            return
    print("False")
    return


s17()