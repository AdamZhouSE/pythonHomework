def judge(s):
    i=0
    list1=list(s)
    a=[]
    ans=0
    while(list1[i]!='@'):
        if list1[i]=='(':
            a.append(list1[i])
        if list1[i]==')':
            if len(a)==0:
                return ans
            del(a[len(a)-1])
        i=i+1
    if len(a)==0:
        ans=1
        return ans
    else:
        return ans
s=input()
ans=judge(s)
if ans==1:
    print('YES',end='')
else:
    print('NO',end='')