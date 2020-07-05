tmp=input().split()
n,k=int(tmp[0]),int(tmp[1])
nali=[]
numli=[]
strli=[]
for i in range(n):
    tp=input().split()
    nali.append(tp[0])
    numli.append(int(tp[1]))
for i in range(k):
    strli.append(input())
nameli=[]
for i in range(n):
    name=''
    ind=i
    while(ind!=0):
        name=name+nali[ind]
        ind=numli[ind]-1
    name=name+nali[ind]
    nameli.append(name)
for i in range(k):
    count=0
    for j in range(len(nameli)):
        if strli[i]==(nameli[j])[:len(strli[i])]:
            count=count+1
    print(count)