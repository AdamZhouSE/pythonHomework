T =int(input())
for p in range(T):
    n = int(input())
    import re
    strr = input()
    lllist = re.split(",| ",strr)
    # numList = [int(x) for x in input().split(",|")]
    numList = []
    for i in lllist:
        numList.append(int(i))
    if(n<=3):
        print("no pairs")
    else:
        res = []
        for i in range(n-3):
            for j in range(i+1,n-2):
                for m in range(j+1,n-1):
                    for n in range(m+1,n):
                        A,B,C,D = numList[i],numList[j],numList[m],numList[n]
                        if(A+B==C+D):
                            res.append([i,j,m,n])
        if(len(res)==0):
            print("no pairs")
        else:
            for i in range(0,3):
                print(res[i],end=" ")
            print(res[-1])
