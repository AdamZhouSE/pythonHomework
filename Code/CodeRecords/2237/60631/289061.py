s=input().split(' ')
data=[]
for i in range(1,int(s[0])+1):
    data.append(i)
#print(data)
for j in range(int(s[1])):
    d=input().split(' ')
    l=int(d[0])-1
    r=int(d[1])
    tp=data[0:l]
    tm=data[l:r]
    tmm=[]
    for i in reversed(tm):
        tmm.append(i)
    tm=tmm
    te=data[r:]
    data=tp+tm+te
for i in data:
    print(i,end=' ')
    