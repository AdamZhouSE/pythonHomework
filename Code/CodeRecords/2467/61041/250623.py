T = eval(input())
arr = []
for i in range(0,T):
    mnk = input()
    stra = input()
    strb = input()
    m = int(mnk[0])
    n = int(mnk[2])
    k = int(mnk[4])
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
    cnt = 0
    while cnt<len(strb):
        if strb[cnt]==' ':
            cnt+=1
        else:
            temp = strb[cnt]
            while cnt!=len(strb)-1 and strb[cnt+1]!=' ':
                cnt+=1
                temp = temp + strb[cnt]
            arr.append(int(temp))
            cnt+=1
    arr = sorted(arr)
    print(arr[k-1])