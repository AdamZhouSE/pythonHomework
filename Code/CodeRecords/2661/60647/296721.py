n=int(input())
for i in range(n):
    a=int(input())
    b=0
    c=0
    strr=bin(a).replace('0b','')
    for j in strr:
        if j=='0':
            b+=1
        else:
            c+=1
    d=b^c 
    print(d)