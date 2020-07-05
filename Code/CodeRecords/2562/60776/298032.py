a=int(input())
for i in range(0,a):
    b=int(input())
    b=bin(b)
    b=b.replace("0b","")
    if len(b)%2==1:
        b="0"+b
    c=[]
    for j in range(0,len(b)):
        c.append(b[j])
    b=c
    for j in range(0,int(len(b)/2)):
        temp=b[2*j+1]
        b[2*j+1]=b[2*j]
        b[2*j]=temp
    b="0b0"+"".join(b)
    a=int(b,2)
    print(a)