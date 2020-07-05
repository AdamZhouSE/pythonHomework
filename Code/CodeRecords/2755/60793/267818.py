for test in range(0, int(input())):
    input()
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    l1, l2 = len(ls1), len(ls2)
    ls3 = [0 for x in range(0, l1 + l2 - 2)]
    for i in range(0, l1):
        for j in range(0, l2):
            ls3[i + j] += ls1[i] * ls2[j]
    for i in ls3:
        print(i, end=" ")
    print(ls3[-1])