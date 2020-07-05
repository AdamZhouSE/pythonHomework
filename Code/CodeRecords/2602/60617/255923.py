def main():
    A=list(map(str, eval(input())))
    B=list(map(str, eval(input())))
    A="".join(A)
    B="".join(B)
    Breadth=len(A)
    while Breadth>=1:
        bfs(A, B, Breadth)
        Breadth-=1
    print(0)

def bfs(strA, strB , Breadth):
    moveTimes=len(strA)-Breadth
    if moveTimes==0:
        if strA==strB:
            print(Breadth)
            exit()
        return
    for i in range(0, moveTimes+1):
        subString=strA[i:Breadth+i]
        if subString in strB:
            print(len(subString))
            exit()



if __name__=='__main__':
    main()