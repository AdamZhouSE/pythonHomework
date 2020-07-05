T = eval(input())
for i in range(0,T):
    arr = []
    N = eval(input())
    stra = input()
    cnt = 0
    while cnt<len(stra):
        if stra[cnt]==' ':
            cnt+=1
        else:
            temp = stra[cnt]
            while cnt!=len(stra)-1 and stra[cnt+1]!=' ':
                cnt+=1
                temp = temp + stra[cnt]
            arr.append(int(temp))
            cnt+=1
    for j in range(0,len(arr)):
        temp = 1
        for x in range(0,len(arr)):
            if j!=x:
                temp = temp*arr[x]
            else:
                continue
        if j==len(arr)-1:
            print(temp,end=' ')
            print()
        else:
            print(temp,end=' ')