def merge(new,q):
    return [new[0],q[1]]

l=input().split("],[")
new=input().split(",")
l[0]=l[0][2:len(l[0])]
l[-1]=l[-1][0:-2]
new[0]=new[0][1:len(new[0])]
new[-1]=new[-1][0:-1]
qs=[]
for i in l:
    k=i.split(",")
    qs.append([int(k[0]),int(k[1])])
new_q=[int(new[0]),int(new[-1])]
k=0
#print(qs)
#print(new_q)
for i in range(len(qs)):
    if new_q[0]<=qs[i][0]:
        k=i
        break
    k=len(qs)
if k==0:
    qs.insert(k,new_q)
else:
    if qs[k-1][1]>=new_q[0]:
        new_q=[qs[k-1][0],new_q[1]]
        del qs[k-1]
        qs.insert(k-1,new_q)
    else:
        qs.insert(k,new_q)
i=k
while(i<len(qs)):
    if qs[k - 1][1] < new_q[0]:
        if i==k:
            i+=1
        else:
            if qs[i][0]<=new_q[1]:
                if qs[i][1]<=new_q[1]:
                    del qs[i]
                else:
                    new_q=merge(new_q,qs[i])
                    del qs[i-1]
                    del qs[i-1]
                    qs.insert(i-1,new_q)
            else:
                break
    else:
        if qs[i][0] <= new_q[1]:
            if qs[i][1] <= new_q[1]:
                del qs[i]
            else:
                new_q = merge(new_q, qs[i])
                del qs[i - 1]
                del qs[i - 1]
                qs.insert(i - 1, new_q)
        else:
            break
print(qs)


