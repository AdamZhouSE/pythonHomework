n=int(input())
for i in range(n):
    res=[]
    number=int(input())
    nums=list(map(int,input().split(" ")))

    Numsdict={}

    for j in nums:
        if j in Numsdict:
            Numsdict[j]+=1
        else:
            Numsdict[j]=1

    key=list(Numsdict.keys())
    value=list(Numsdict.values())

    i=0
    while i<len(value):
        tmp=[key[i],value[i]]
        j=len(res)-1
        while j>=0:
            if tmp[1]>res[j][1]:
                j-=1
                continue
            elif tmp[1]==res[j][1]:
                if tmp[0]<res[j][0]:
                    j-=1
                    continue
                else:
                    break
            else:
                break
        if j==len(res)-1:
            res.append(tmp)
        else:
            res.insert(j+1,tmp)
        i+=1

    result=""
    for i in res:
        result+=(str(i[0])+" ")*i[1]
    print(result)