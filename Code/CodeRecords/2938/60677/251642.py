def smaller(a,b):
    alist=list(str(a))
    blist=list(str(b))
    if alist[0]<blist[0]:
        return a
    if alist[0]>blist[0]:
        return b
    else:
        for i in range(alist.__len__(),3):
            alist.append("0")
        for i in range(blist.__len__(),3):
            blist.append("0")
        aup="".join(alist)
        bup="".join(blist)
        if aup<bup:
            return a
        if aup>bup:
            return b
        else:
            if a<b:
                return a
            else:
                return b

answer=[i+1 for i in range(100)]
for i in range(0,99):
    for j in range(i+1,100):
        if smaller(answer[i],answer[j])==answer[j]:
            swap=answer[i]
            answer[i]=answer[j]
            answer[j]=swap

for i in answer:
    print(i)