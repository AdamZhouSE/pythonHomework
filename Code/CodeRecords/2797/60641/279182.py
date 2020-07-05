def main():
    ranges = eval(input())
    ranges = sorted(ranges, key=lambda x: x[0])

    for i in range(0, len(ranges) - 1):
        try:
            while True:
                if ranges[i][1] >= ranges[i + 1][0]:
                    ranges[i] = [ranges[i][0], ranges[i + 1][1]]
                    del ranges[i + 1]
                else:
                    break
        except IndexError:
            break

    print(ranges)


if __name__ == "__main__":
    main()
