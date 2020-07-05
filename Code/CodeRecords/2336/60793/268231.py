for test in range(0, int(input())):
    k = list(map(int, input().split()))[-1]
    a = list(map(int, input().split()))
    result = []
    for i in range(0, len(a) - k + 1):
        sub_ls = a[i:i + k]
        result.append(max(sub_ls))
    for x in result:
        print(x, end=" ")
    print()