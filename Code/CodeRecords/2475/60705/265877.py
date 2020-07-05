def isconsective(arr):
    res = True
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            res = False
    return res


if __name__ == '__main__':
    test = int(input())
    for i in range(0, test):
        length = int(input())
        arr = list(map(int, input().split(" ")))
        arr.sort()
        m = 1
        for j in range(0, len(arr)):
            for k in range(j+1, len(arr) + 1):
                if isconsective(arr[j:k]) and k - j > m:
                    m = k - j
        print(m)

