for test in range(0, int(input())):
    input()
    temp_ls1 = list(input().split())
    result = 0
    for string in temp_ls1:
        for c in string:
            result += int(c)
    print(result % 3 == 0)