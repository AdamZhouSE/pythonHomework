def reverse(num):
    ls=[]
    le=len(num)-1
    while le>=0:
        ls.append(num[le])
        le-=1
    return ls
T=int(input())
while T>0:
    n,k=map(int,input().split())
    num=[int(n) for n in input().split()]
    re=[]
    c=0
    while c<len(num):
        cc=[]
        if c+k>=len(num):
            cc=reverse(num[c:])
        else:
            cc=reverse(num[c:c+k])
        for i in cc:
            re.append(i)
        c+=k
    count=0
    for i in re:
        count+=1
        if count==len(re):
            print(i,end=' \n')
        else:
            print(i,end=' ')
    T-=1