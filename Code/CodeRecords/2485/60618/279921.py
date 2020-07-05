t=int(input())
for i in range(0,t):
    n=int(input())
    word=[str(n) for n in input().split()]
    for j in range(0,n):
        wlist=list(word)
        for m in range(1,len(word[j])):
            for k in range(0,len(word[j])-m):
                if word[k]>word[k+1]:
                    word[k],word[k+1]=word[k+1],word[k]
        word[j]=''.join(wlist)
    nlist=list(set(word))
    re=[]
    for j in range(0,len(nlist)):
        re.append(word.count(nlist[i]))
    string=''
    for j in range(1,len(re)):
        for k in range(0,len(re)-j):
            if re[k]>re[k+1]:
                re[k],re[k+1]=re[k+1],re[k]
    for j in range(0,len(re)):
        string=string+" "+str(re[j])
    print(string[1:])
        
    