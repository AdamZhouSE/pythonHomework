n=int(input())
for i in range(n):
    le=int(input())
    row1=[int(n) for n in input().split()]
    row2=[int(n) for n in input().split()]
    if le==1 and row1[0]==row2[0]:
        print("YES")
    elif le==1 and row1[0]!=row2[0]:
        print("NO")
    else:
        xc = []
        for index in range(le):
            xc.append(row1[index] - row2[index])
        cunzai = True
        k=0
        for index in range(1, le - 1):
            if xc[index]==0:
                k+=1
            if xc[index] != xc[index - 1] and xc[index] != xc[index + 1]:
                cunzai = False
                print("NO")
                break
        if xc[len(xc)-1]>xc[len(xc)-2] and k==le-2:
            cunzai=False
            print("NO")
        if cunzai:
            print("YES")
