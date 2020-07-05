def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        result = []
        for j in range(0, num + 1):
            if j & num == j:
                result.insert(0, str(j))
        print(" ".join(result) + " ")


if __name__ == '__main__':
    main()
