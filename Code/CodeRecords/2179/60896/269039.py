m=input()
m=m.split(' ')
n=eval(m[1])
m=eval(m[0])
s=input()
def find_longest_prefix(x,y):
    count=0
    t=min(len(x),len(y))
    for i in range(0,t):
        if(x[i]==y[i]):
            count+=1
        else:return i
    return t
for i in range(0,m):
    maxnum=0;
    a=input()
    a=a.split(' ')
    b=int(a[1])
    c=int(a[2])
    d=int(a[3])
    a=int(a[0])
    temps1=s[a-1:b]
    temps2=s[c-1:d]
    for i in range(0,len(temps1)):
        temp=temps1[:i+1]
        k=find_longest_prefix(temps1,temps2)
        maxnum=max(k,maxnum)
    print(maxnum)