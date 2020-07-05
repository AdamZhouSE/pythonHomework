for test in range(0, int(input())):
    input()
    ls1 = sorted(list(map(int, input().split())))
    ls2 = sorted(list(map(int, input().split())))
    ls3 = sorted([ls1[i] - ls2[i] for i in range(0, len(ls1))])
    print(max(-ls3[0], ls3[-1]))