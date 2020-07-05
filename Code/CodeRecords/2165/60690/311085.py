def BFS(res,dict,begin):
    if begin=='':return
    l=dict[begin]
    next=''
    count=0
    for i in range(len(l)):
        if l[i]==1:
            count+=1
            if chr(ord('a')+i) not in res:
                res.append(chr(ord('a')+i))
            dict[begin][i]=0
            dict[chr(ord('a')+i)][ord(begin)-ord('a')]=0
            if count==1:
                next=chr(ord('a')+i)
    BFS(res,dict,next)


t=int(input())
finalRes=[]
for i in range(t):
    s=input().split(" ")
    N=int(s[0])
    begin=s[1]
    nodes=input().split(" ")
    dict={}
    for j in range(N):
        s=input().split(" ")
        l=[int(s[1]),int(s[2]),int(s[3]),int(s[4])]
        dict[s[0]]=l
    res = [begin]
    BFS(res,dict,begin)
    finalRes.append(res)
for i in range(len(finalRes)):
    l=finalRes[i]
    for j in range(len(l)-1):
        print(l[j],end=" ")
    print(l[-1])
