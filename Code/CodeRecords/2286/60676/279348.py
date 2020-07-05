if __name__ == '__main__':
    t = input().split()
    arr = [1 for i in range(int(t[0]) + 1)]
    for i in range(int(t[1])):
        tmp = input().split()
        for j in range(int(tmp[0]), int(tmp[1])+1):
            arr[j] = 0
    num = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            num += 1
    print(num)