def encode(a):
    index=2
    res=a%2
    while(int(a/10)!=0):
        a=int(a/10)
        res=res+a%10*index
        index*=2
    return res
o=input()
n=[]
for i in range(1,len(o)-1):
    if(o[i]!=','):
        n.append(o[i])
s="".join(n)
a=int(s)
print(encode(a))