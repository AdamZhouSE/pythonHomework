n = int(input())
l = []
for i in range(n):
    length=int(input())
    temp =list(map(int,input().split()))
    temp.sort()
    l.append(temp)
for i in range(n):
    find =False
    if l[i][len(l[i])-1]<=0:
        print(1)
    else:
        firstPositiveNum = -1
        hasZero = False
        for j in range(len(l[i])-1):
            if l[i][j]==0:
                hasZero = True
            if l[i][j]<=0 and l[i][j+1]>0:
                firstPositiveNum = j+1
            elif l[i][0]>0:
                firstPositiveNum = 0
            if l[i][j]>0 and (l[i][j+1]!=l[i][j]+1 and l[i][j+1]!=l[i][j]):
                print(l[i][j]+1)
                find=True
                break
        if find==False:
            if  l[i][firstPositiveNum]==1 :
                
                print (l[i][len(l[i])-1]+1) 
            else:
                if hasZero:
                    print(1)
                else:
                    print(l[i][firstPositiveNum]-1)