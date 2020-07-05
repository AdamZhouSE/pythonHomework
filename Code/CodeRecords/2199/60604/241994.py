def opr(s,k):
    tmp=[]
    res=[]
    for i in range(len(s)-1,0,-1):
        for j in range(len(s)-i+1):

            if not s[j:j+i] in tmp and not s[j:j+i] in res:
                tmp.append(s[j:j+i])
            else:
                res.append(s[j:j+i])
    res.append(k+1)
    return res
s=input()
#print(s)


res=opr(s,0)
while(len(res)>1):
    a=[]
    
#    print(res)
    for i in range(len(res)-1):
        tmp=opr(res[i],res[-1])
        for j in range(len(tmp)-1):
            if not tmp[j] in a:
                a.append(tmp[j])
    a.append(tmp[-1])
    res=a
print(res[0])