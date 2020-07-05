for test in range(0, int(input())):
    input()
    ls = list(map(int, input().split()))
    result = 0
    for i in range(1, len(ls) + 1):
        for j in range(0, len(ls) - i + 1):
            ls_slice = ls[j:j+i]
            if result < i * min(ls_slice):
                result = i * min(ls_slice)
    print(result)