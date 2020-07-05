def main():
    A = list(map(int, input().split(",")))
    B = list(map(int, input().split(",")))
    C = list(map(int, input().split(",")))
    D = list(map(int, input().split(",")))
    n = len(A)
    result = 0
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                for l in range(0, n):
                    if A[i] + B[j] + C[k] + D[l] == 0:
                        result += 1
    print(result)


if __name__ == '__main__':
    main()
