def solution(words:list):
    words=sorted(words,key=len,reverse=True)
    lst=[sorted(list(i)) for i in words]
    maxLen=len(words[0])
    level=[words[i] for i in range(len(words)) if len(words[i])==maxLen]
    res=[[i] for i in level]
    while len(level)!=0:
        for curr in level:
            next_level=[]
            level.remove(curr)
            for i in range(len(curr)):
                shorter=curr[:i]+curr[i+1:]
                if sorted(list(shorter)) in lst:
                    p=lst.index(sorted(list(shorter)))
                    for tmp in res:
                        if tmp[-1]==curr:
                            tmp.append(words[p])
                    next_level.append(words[p])
            if len(next_level)==0:continue#上面的exp2
            level=next_level
    return res



if __name__=="__main__":
    s=input()
    words=[s]
    k=0
    while k<20:
        try:
            s=input()
            words.append(s)
            k+=1
        except EOFError:
            break
    ans=solution(words)
    ans=list(sorted(ans,key=len,reverse=True))
    tgt=sorted(ans[0],key=len)
    print(len(tgt))
    for i in tgt:
        print(i)