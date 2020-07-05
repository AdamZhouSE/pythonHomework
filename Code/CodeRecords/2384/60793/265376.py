test_num = int(input())
for test in range(0, test_num):
    input()
    a = list(map(int, input().split()))
    sorted(a)
    for i in a:
        if i >= 0:
            if i + 1 not in a:
                print(i + 1)
                break