def bin(a):
    res=a%10
    index=10
    while(int(a/2)!=0):
        a=int(a/2)
        res=res+a%2*index
        index=index*10
    return res
def encode(a):
    index=2
    res=a%2
    while(int(a/10)!=0):
        a=int(a/10)
        res=res+a%10*index
        index*=2
    return res
def fan(a):
    b=str(a)
    li=[]
    for i in range(0,len(b)):
        if(b[i]=='0'):
            li.append('1')
        else:
            li.append('0')
    s="".join(li)
    res=int(s)
    return res

num=int(input())
li=[]
for i in range(num):
    a=int(input())
    b=bin(a)
    c=fan(b)
    d=encode(c)
    print(d)