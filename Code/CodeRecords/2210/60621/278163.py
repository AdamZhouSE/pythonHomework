a=input()
answer=[]
for i in range(int(a)):
    b={}
    c={}
    bs=input()
    cs=input()

    for j in cs:
        if j in c:
            c[j]+=1
        else:
            c[j]=1
            b[j]=0
    head,appendage=0,0
    def check():
        for j in c.keys():
            if b[j]<c[j]:
                return False

        return True
    b[bs[0]]=1
    minmum=len(bs)+1
    ans=""
    while appendage<len(bs):
        if check():
            if minmum>appendage-head+1:
                minmum=min(minmum,appendage-head+1)
                ans=bs[head:appendage+1]
            head += 1
            if bs[head-1] in cs:
                b[bs[head-1]]-=1
        else:
            appendage+=1
            if appendage>=len(bs):
                break
            else:
                if bs[appendage] in cs:
                    b[bs[appendage]]+=1

    if minmum<=len(bs):
        answer.append(ans)
    else:
        answer.append("-1")
for i in range(int(a)):
    if i!=int(a)-1:
        print(answer[i],end="")
        print("\n",end="")
    else:
        print(answer[i],end="")
        print("\n",end="")
 