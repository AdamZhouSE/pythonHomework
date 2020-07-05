if __name__ == "__main__":
    n,root = map(int,input().split(" "))
    dict = {}
    for i in range(n):
        r, lc, rc = map(int,input().split(" "))
        dict[r] = [lc, rc]
    lst = [root]
    reverselst = []
    index = 1
    while lst != []:
        print("Level " + str(index) + " : ",end="")
        print(*lst)
        if index % 2 == 0:
            reverselst.append(reversed(lst))
        else:
            reverselst.append(lst)
        newlst = []
        for no in lst:
            temp = dict[no]
            if temp[0] != 0:
                newlst.append(temp[0])
            if temp[1] != 0:
                newlst.append(temp[1])
        lst = newlst
        index += 1
    for j in range(1,index):
        if j % 2 == 1:
            print("Level " + str(j) + " from left to right: ", end="")
        else:
            print("Level " + str(j) + " from right to left: ", end="")
        print(*reverselst[j-1])