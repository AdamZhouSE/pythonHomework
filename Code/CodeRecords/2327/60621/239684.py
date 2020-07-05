a=input()
I=a.count("I")
D=a.count("D")
b=[0]
for i in range(len(a)):
    b.append(i+1)
b1=[i for i in b[0:I]]
b2=[j for j in b[I:]]
b2.sort(reverse=True)

c=[];cu1,cu2=0,0
for i in a:
    if i=="I":

        c.append(b1[cu1])
        cu1+=1
    else:
        c.append(b2[cu2])
        cu2+=1
if(cu1!=len(b1)):
    c.append(b1[len(b1)-1])
else:
    c.append(b2[len(b2)-1])
print(c)