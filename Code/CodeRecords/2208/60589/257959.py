t=int(input())
for i in range(t):
    n=int(input())
    a=input().split(' ')
    a=list(map(int,a))
    ans=[]
    for j in range(len(a)):
        if j==0:
            ans.append(-1)
            continue
        this=a[j]
        before=a[:j]
        before=list(filter(lambda x:x<this,before))
        if len(before)>0:
            ans.append(before.pop())
        else:
            ans.append(-1)
    ans=list(map(str,ans))
    print(' '.join(ans)+' ')