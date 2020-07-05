def cut(s:str):
    results=[]
    num=0
    for x in range(len(s)):
        for i in range(len(s)-x):
            results.append(s[i:i+x+1])
    return results
n=int(input())
res=[]
for i in range(0,n):
    list1=input().split(' ')
    str1=list1[0]
    if len(str1)>20:
        print(-1)
        print(93)
        break
    else:
        k=int(list1[1])
        zichuan=cut(str1)
        klist=[]
        lenlist=[]
        for j in zichuan:
            if zichuan.count(j)==k:
                if j not in klist:
                    klist.append(j)
                    lenlist.append(len(j))
        if len(lenlist)==0:
            print(-1)
        else:
            lenlist.sort()
            maxcount=0
            maxlen=0
            for j in lenlist:
                if lenlist.count(j)>=maxcount:
                    maxlen=j
                    maxcount=lenlist.count(j)
            print(maxlen)