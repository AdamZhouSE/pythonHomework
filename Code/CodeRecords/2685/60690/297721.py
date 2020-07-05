t=int(input())
res=[]
for i in range(t):
    given=int(input())
    copy=10**given
    num=0
    bits=[]
    while given>0:
        if given>9:
            bits.append(9)
        else:
            bits.append(given)
        given-=9
    for j in range(len(bits)):
        num+=bits[j]*copy
        copy*=10
    res.append(num)
for  e in res:print(e)