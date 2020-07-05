def func22():
    in_str = input()[1:-1]
    i = 0
    matrix = []
    while i < len(in_str):
        temp = []
        while in_str[i] != "]":
            j = i
            while in_str[i].isdigit():
                i += 1
            if j != i:
                temp.append(int(in_str[j:i]))
            else:
                i += 1
        matrix.append(temp)
        i += 2
    m = len(matrix)
    n = len(matrix[0])
    for k in range(-n+1, m-1):
        candi = []
        for x in range(n):
            if x+k >= 0 and x+k < m:
                candi.append(matrix[x+k][x])
        candi.sort(reverse=True)
        for x in range(n):
            if x+k >= 0 and x+k < m:
                matrix[x+k][x] = candi.pop()
    print(matrix)

    return

func22()