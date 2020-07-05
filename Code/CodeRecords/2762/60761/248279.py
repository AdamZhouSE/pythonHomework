def moveAndDirection(move,n):
    x=y=0
    preDirection="N"
    directionDict={"NU":"N","ND":"S","NR":"E","NL":"W",
                  "SU":"S","SD":"N","SR":"W","SL":"E",
                  "WU":"W","WD":"E","WR":"N","WL":"S",
                  "EU":"E","ED":"W","ER":"S","EL":"N"}
    ctDirection=""
    for i in range(0,2*n,2):
        ctDirection=directionDict[preDirection+move[i]]
        if ctDirection=="N":
            y=y+int(move[i+1])
        elif ctDirection=="S":
            y=y-int(move[i+1])
        elif ctDirection=="E":
            x=x+int(move[i+1])
        elif ctDirection=="W":
            x=x-int(move[i+1])
        preDirection=ctDirection
    return str(int((x**2+y**2)**0.5))+" "+ctDirection

t=int(input())
for i in range(t):
    n=int(input())
    move=list(map(str,input().split(" ")))
    print(moveAndDirection(move,n))