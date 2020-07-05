def main():
    num = int(input())
    result = [0]
    for i in range(0, num):
        degree = int(input())
        l = len(result)
        for j in range(0, l):
            result.append(result[0] + degree)
            result.append(result[0] - degree)
            del result[0]
    if 0 in result:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
