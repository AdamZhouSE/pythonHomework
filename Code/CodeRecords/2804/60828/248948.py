def h_3_1():
    def SWAP(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    s = input()
    arr = s.split("+")
    l = len(arr)
    for i in range(0, l):
        for j in range(i, l):
            if (arr[i] >= arr[j]):
                SWAP(arr, i, j)
            j = j + 1
        i = i + 1
    res = []
    for i in range(0, l):
        res += arr[i]
        if (i != l - 1): res += "+"

    res = "".join(str(i) for i in res)
    print(res)
    
if __name__ == '__main__':
    h_3_1()
    # for i in range(0, l):
    #     if (i != l - 1):
    #         print(arr[i], end="+")
    #     else:
    #         print(arr[i], end="+")


if __name__ == '__main__':
  h_3_1()