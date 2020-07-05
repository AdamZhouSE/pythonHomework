read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
for i in range(len(ns)):
    if (not i or ns[i] > ns[i - 1]) and (i == len(ns) - 1 or ns[i] > ns[i + 1]):
        print(i)
        exit(0)