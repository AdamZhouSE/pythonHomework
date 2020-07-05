def student_num(X, G):
    return X * (-1) - 1 + G


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        arr = [int(j) for j in input().split()]
        print(student_num(arr[0], arr[1]))