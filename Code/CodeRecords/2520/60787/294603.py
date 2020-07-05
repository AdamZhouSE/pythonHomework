R=int(input())
C=int(input())
r=int(input())
c=int(input())
length=[]
co=[]
for i in range(0,R):
    for j in range(0,C):
        temp=abs(r-i)+abs(c-j)
        length.append(temp)
        co.append([i,j])
for i in range(0,len(length)):
    for j in range(0,len(length)-1):
        if length[j]>length[j+1]:
            length[j],length[j+1]=length[j+1],length[j]
            co[j],co[j+1]=co[j+1],co[j]
print(co)