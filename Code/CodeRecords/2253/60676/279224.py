if __name__ == '__main__':
    t = input().split()
    arr = input().split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    res = []
    for i in range(int(t[1])):
        opr = input().split()
        opt = int(opr[0])
        if opt == 3:
            arr[int(opr[1])-1] = int(opr[2])
        else:
            tmp = arr[int(opr[1])-1:int(opr[2])]
            tmp.sort()
            arg = int(opr[3])
            if opt == 1:
                index = 0
                while index < len(tmp) and tmp[index] < arg:
                    index += 1
                res.append(index + 1)
            elif opt == 2:
                res.append(tmp[arg - 1])
            elif opt == 4:
                index = 0
                while index < len(tmp) and tmp[index] < arg:
                    index += 1
                res.append(tmp[index - 1])
            else:
                index = 0
                while index < len(tmp) and tmp[index] <= arg:
                    index += 1
                res.append(tmp[index])
    for i in range(len(res)):
        print(res[i])