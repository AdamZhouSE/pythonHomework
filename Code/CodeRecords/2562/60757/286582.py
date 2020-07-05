t=int(input())
li=input().split()
N=int(li[0])
Q=int(li[1])
arr=list(map(int,input().split()))
un=[]
r=[]
tr=[]
for i in range(1,N+1):
    un.append(i)
for i in range(Q):
    form=arr[i*2]
    idd=arr[i*2+1]
    if(form==1):
        del un[un.index(idd)]
        r.append(idd)
    elif(form==2):
        del r[r.index(idd)]
        tr.append(idd) 
    elif(form==3):
        del un[un.index(idd)]
        tr.append(idd)
    else:
        del tr[tr.index(idd)]
        r.append(idd)
if len(un)==0:
    print('EMPTY')
else:
    for i in range(len(un)):
        print(un[i],end=' ')
print()
if len(r)==0:
    print('EMPTY')
else:
    for i in range(len(r)):
        print(r[i],end=' ')
print()
if len(tr)==0:
    print('EMPTY')
else:
    for i in range(len(tr)):
        print(tr[i],end=' ')
print()