for test in range(0, int(input())):
    input()
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    ls3 = set(ls1) | set(ls2)
    for x in ls3[:-1]:
        print(x, end=" ")
    print(ls3[-1])