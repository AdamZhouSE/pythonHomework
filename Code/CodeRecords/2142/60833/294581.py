for i in range(0,int(input())):
    s=input()
    left=[]
    res=[]
    count=0
    for j in s:
        if j=='(':
            count+=1
            left.append(count)
            res.append(count)
        elif j==')':
            res.append(left[-1])
            left=left[0:-1]
    for j in res:
        print(j, end=' ')
    print('')