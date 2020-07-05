def func():
    tArr = input()
    tArr = [int(n) for n in tArr.split(" ")]
    n = int(tArr[0])
    m = int(tArr[1])
    strArr = [""] * n
    i = 0
    while i < n:
        strArr[i] = input()
        i += 1

    beg = [0, 0]
    beg_flag = False  # found beg or not
    end = [0, 0]

    i = 0
    while i < n:
        break_flag = False
        j = 0
        while j < m:
            if not beg_flag:
                if strArr[i][j] == "B":
                    beg = [i+1, j+1]
                    beg_flag = True
                    if j == m - 1:
                        end = [i+1, j+1]
                        break_flag = True
                        break
            else:
                if strArr[i][j] == "W":
                    end = [i+1, j]
                    break_flag = True
                    break
                if j == m - 1:
                    end = [i+1, j+1]
                    break_flag = True
                    break
            j += 1
        if break_flag:
            break
        i += 1

    dis = (end[1] - beg[1]) // 2
    pos = [beg[0]+dis, beg[1]+dis]
    print(str(pos[0]) + " " + str(pos[1]))


func()
