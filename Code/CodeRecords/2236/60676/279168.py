if __name__ == '__main__':
    arr = []
    res = []
    for i in range(int(input())):
        opr = input().split()
        opt = int(opr[0])
        num = int(opr[1])
        if opt == 1:
            arr.append(num)
            arr.sort()
        elif opt == 2:
            arr.remove(num)
        elif opt == 3:
            res.append(arr.index(num) + 1)
        elif opt == 4:
            res.append(arr[num - 1])
        elif opt == 5:
            tmp = 0
            while tmp < len(arr) and arr[tmp] < num:
                tmp += 1
            res.append(arr[tmp - 1])
        else:
            tmp = 0
            while tmp < len(arr) and arr[tmp] <= num:
                tmp += 1
            res.append(arr[tmp])
    for i in range(len(res)):
        print(res[i])