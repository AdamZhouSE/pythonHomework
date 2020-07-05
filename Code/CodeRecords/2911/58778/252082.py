s=input()
sl=s.split( )
n=int(sl[0])
m=int(sl[1])
s=input()
payment=[]
sl.clear()
sl=s.split()
for i in sl:
    payment.append(int(i))
#print(payment)
friend=[]
for i in range(m):
    t=input()
    tl=t.split( )
    A=int(tl[0])
    B=int(tl[1])
    temp=[]
    if(len(friend)==0):
        temp.append(A)
        temp.append(B)
        friend.append(temp)
    else:
        x=0
        for j in friend:
            if(A in j):
                x=1
                j.append(B)
            elif (B in j):
                x=1
                j.append(A)
        if(x==0):
            temp.append(A)
            temp.append(B)
            friend.append(temp)
sum=0
for i in range(n):
    x=0
    for j in friend:
        if(i+1 in j):
            x=1
            break
    if(x==0):
        sum=sum+payment[i]
#print(sum)
for j in friend:
    g=[]
    for x in j:
        g.append(payment[x-1])
    sum=sum+min(g)
#print(friend)
print(sum)
