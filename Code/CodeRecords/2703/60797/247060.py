def find(i, matrix, c):
    for j in range(len(matrix)):
        if (i != j) and (j not in c) and (data[i][j] == 1):
            c.add(j)
            find(j, matrix, c)
        else:
            continue


def findCircleNum(matrix):
    n = len(matrix)
    circles = list()
    count = 0
    c = set()
    i = 0
    while i < len(matrix):
        if i not in c:
            find(i, matrix, c)
            count += 1
            i += 1
        else:
            i += 1
            continue
    return count

if __name__ == "__main__":
    # str = "[[1,1,0], [1,1,0], [0,0,1]]"
    # data = [a for a in str.split(", ")]
    data = [a for a in input().split(", ")]
    for i in range(len(data)):
        data[i]=[int(b) for b in data[i].strip("[]").split(',')]
    re=findCircleNum(data)
    print(re)
