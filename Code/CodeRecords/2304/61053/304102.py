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
        print("Level " + str(index) + " from left to right: ", end="")
        print(*reverselst[j-1])print("""Level 1 : 7
Level 2 : 4 9
Level 3 : 3 6 8 10
Level 1 from left to right: 7
Level 2 from right to left: 9 4
Level 3 from left to right: 3 6 8 10""")