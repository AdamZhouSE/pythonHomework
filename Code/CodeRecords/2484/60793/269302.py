for test in range(0, int(input())):
    input()
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    print(len((set(ls1) | set(ls2))))
