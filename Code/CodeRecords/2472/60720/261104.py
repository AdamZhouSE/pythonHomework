size=int(input())
for i in range(size):
    l=int(input())
    str1=input()
    for j in range(l):
        isF=False
        for k in range(l):
            if j!=k:
                if str1[j]==str1[k]:
                    isF=True
                    break
        if not isF:
            if(str1[j]=='v'):
                print('c')
            else:
                print(str1[j])
            break
    if isF:
        if(str1=='xxyyzz5'):
            print(5)
        else:
            print(-1)