def solution(matrix):
    return 0


if __name__ == '__main__':
    matrix = []
    line = input()
    while line != "]":
        arr = []
        for i in line:
            if i.isdecimal():
                arr.append(i)
        if len(arr) > 0:
            matrix.append(arr)
        line = input()
    print(matrix)
