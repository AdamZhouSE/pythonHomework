x=input()
res=0
tmp1=0
for I in range(1,len(x)+1):
    tmp=x[0:I]
    #print(x[0:I])
    if len(tmp)<3:
        res=0
    else:
        for l in range(2,len(tmp)+1):
            for i in range(len(tmp)-l):
                for j in range(i+1,i+l):
                    #print(tmp[i:i+l],tmp[j:j+l])
                    if tmp[i:i+l]==tmp[j:j+l]:
                        res+=l
    print(res-tmp1)
    tmp1=res