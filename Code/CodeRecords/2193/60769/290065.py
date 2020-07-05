def solve(stri, start, end):
    arr = []
    for i in range(start, end + 1):
        arr.append(stri[:i])
    temp = []
    # print(arr)
    for i in range(end-1, 0, -1):
        for item in arr:
            if len(item) >= i:
                if item[-i:] in temp:
                    return i
                else:
                    temp.append(item[-i:])
        # print(temp)
        temp = []
    return 0


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    stri = input()
    for i in range(m):
        start, end = list(map(int, input().split()))
        print(solve(stri, start, end))
