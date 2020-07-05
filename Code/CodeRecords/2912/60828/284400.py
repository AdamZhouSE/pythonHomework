def h2():
    def isRep(s,left,right):
        isRep = False
        for i in range(left, right):
            for j in range(i + 1, right):
                if (s[i] == s[j]):
                    return True
        return False

    s = list(input())
    isOver = False
    for maxL in range(len(s),0,-1):
        for leftbound in range(0,len(s)-maxL+1):
            if(not isRep(s,leftbound,leftbound+maxL)):
                print(maxL)
                isOver = True
                break
        if (isOver):
            break





if __name__ == '__main__':
    h2()