for test in range(0, int(input())):
    input()
    ls = list(map(int, input().split()))
    result = 0
    for length in range(1, len(ls)):
        for i in range(0, len(ls) - length):
            ls_slice = ls[i:i+length + 1]
            height = min(ls_slice[0], ls_slice[-1])
            temp = height * length
            if temp > result:
                result = temp
    print(result)