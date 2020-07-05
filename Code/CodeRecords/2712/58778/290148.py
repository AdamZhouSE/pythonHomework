m=[]
n=int(input())

def count(st,x):
    t=len(x)
    c=0
    for i in range(t,len(st)+1):
        tmp=st[i-t:i]
        if(tmp==x):
            c+=1
    return c
while n!=0:
    for i in range(n):
        m.append(input())
    st=input()
    re=[]
    for i in m:
        re.append(count(st,i))
    print(max(re))
    for i in range(len(re)):
        if(re[i]==max(re)):
            print(m[i])
    n=int(input())
    m=[]