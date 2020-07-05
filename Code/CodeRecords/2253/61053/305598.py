if __name__ == '__main__':
    n, m = map(int,input().split(" "))
    input()
    lst = list(map(int,input().split(" ")))
    res = []
    for i in range(m):
        oplst = list(map(int,input().split(" ")))
        if oplst[0] == 1:
            rank = 1
            for k in range(oplst[1]-1,oplst[2]):
                if lst[k] < oplst[3]:
                    rank+=1
            res.append(rank)
        elif oplst[0] == 2:
            temp = lst[oplst[1]-1:oplst[2]]
            temp = sorted(temp)
            res.append(temp[oplst[3]-1])
        elif oplst[0] == 3:
            lst[oplst[1]-1] = oplst[2]
        elif oplst[0] == 4:
            temp = lst[oplst[1] - 1:oplst[2]]
            temp = sorted(temp)
            index = 0
            while index < len(temp):
                if temp[index] >= oplst[3]:
                    break
                index += 1
            res.append(temp[index-1])
        elif oplst[0] == 5:
            temp = lst[oplst[1] - 1:oplst[2]]
            temp = sorted(temp)
            index = len(temp)-1
            while index >= 0:
                if temp[index] <= oplst[3]:
                    break
                index -= 1
            res.append(temp[index + 1])

    for no in res:
        print(no)