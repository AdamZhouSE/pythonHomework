def main():
    num_of_bugs, num_of_debugs = map(int, input().split(" "))
    graph = [[10000 for i in range(0, 2 ** num_of_bugs + 1)] for j in range(0, 2 ** num_of_bugs + 1)]
    solutions = []
    data = []
    for i in range(0, num_of_debugs):
        time, bn, fn = input().split(" ")
        data.append(time + " " + bn + " " + fn)
    print(data)


if __name__ == '__main__':
    main()
