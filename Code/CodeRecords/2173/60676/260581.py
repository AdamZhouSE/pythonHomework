if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        n = int(input())
        result.append(n * (n + 1) * (2 * n + 1) // 6)
    for i in range(len(result)):
        print(result[i])