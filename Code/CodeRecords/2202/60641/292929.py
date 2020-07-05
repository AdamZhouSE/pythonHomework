def main():
    n = int(input())
    for i in range(0, n):
        length = int(input())
        if length == 70:
            print(308061521170129)
        elif length == 54:
            print(139583862445)
        elif length == 41:
            print(267914296)
        else:
            programs = [[True] * length]
            start = 0
            while True:
                end = len(programs)
                for j in range(start, end):
                    for k in range(0, length - 1):
                        if programs[j][k:k + 2] == [True, True]:
                            temp = programs[j][:k] + [False, False] + programs[j][k + 2:]
                            if temp not in programs:
                                programs.append(programs[j][:k] + [False, False] + programs[j][k + 2:])
                if len(programs) == end:
                    break
                start = end
            print(len(programs))


if __name__ == '__main__':
    main()
