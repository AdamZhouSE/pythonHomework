for test in range(0, int(input())):
    input()
    ls = list(map(int, input().split()))
    result = 0
    for length in range(0, len(ls)):
        for i in range(0, len(ls) - length + 1):
            ls_slice = ls[i:i+length]
            height = min(ls_slice[0], ls_slice[-1])
            temp = height * length
            if temp > result:
                result = temp
    print(result)