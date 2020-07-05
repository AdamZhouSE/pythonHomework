def ch(x):
    for i in range(0,16-len(x)):
        x="0"+x
    return x
def xor(b,c):
    d=""
    bb=ch(bin(b).replace("0b",''))
    cc=ch(bin(c).replace("0b",''))
    for i in range(0,len(bb)):
        if bb[i]==cc[i]:
            d=d+"0"
        else:
            d=d+"1"
    return int(d,2)
n=int(input())
for p in range(n):
    num=int(input())
    a=[int(x) for x in input().split(" ")]
    res=""
    for j in range(0,len(a)-1):
        res=res+str(xor(a[j],a[j+1]))+" "
    res=res+str(a[len(a)-1])
    print(res)