for i in range(0,int(input())):
    str1=input()
    asc=[]
    for j in str1:
        asc.append(ord(j))
    asc.sort(reverse=True)
    cha=asc[1]-asc[0]
    length=len(asc)
    k=0
    j=2
    res=[]
    while(j<length):
        if asc[j]-asc[j-1]!=cha:
            cha=asc[j]-asc[j-1]
            if j-k>len(res):
                res=asc[k:j]
            k=j-1
        else:
            if j==length-1:
                if j-k+1>len(res):
                    res=asc[k:j+1]
        j+=1
    for j in res:
        print(chr(j),end='')
    print('')