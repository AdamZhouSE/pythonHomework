def com(a,b):
    a1=a.split(' ')
    b1=b.split(' ')
    x1=int(a1[0])
    y1=int(a1[1])
    x2=int(b1[0])
    y2=int(b1[1])

    if(x1==x2):
        return 100000
    else:
        return ((y1-y2)/(x1-x2))

n=input().split(' ')
num1=int(n[0])
num2=int(n[1])
num3=int(n[2])
s=str(num2)+" "+str(num3)
li=[]
for i in range(num1):
    r=input()
    li.append(com(r,s))
li=list(set(li))
print(len(li))