T =int(input())
for p in range(T):
    nn = int(input())
    import re
    strr = input()
    if("," in strr):
        numList = [int(x) for x in strr.split(",")]
    else:
        numList = [int(x) for x in strr.split()]
    if(nn<=3):
        print("no pairs")
    else:
        res = []
        for i in range(nn):
            for j in range(0,nn):
                if(j==i): continue
                for m in range(0,nn):
                    if(m==j or m==i):
                        continue
                    for n in range(0,nn):
                        if(n==m or n==j or n==i):
                            continue
                        A,B,C,D = numList[i],numList[j],numList[m],numList[n]
                        if(A+B==C+D):
                            res.append([i,j,m,n])
        if(len(res)==0):
            print("no pairs")
        else:
            for i in range(0,3):
                print(res[0][i],end=" ")
            print(res[0][-1])

