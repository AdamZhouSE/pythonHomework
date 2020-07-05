l=eval(input())
m=[0 for i in range(len(l))]
for i in range(len(l)):
    flag=0
    mm=0
    for k in range(i+1,len(l)):
        for j in l[i]:
            if j in l[k]:
                flag=1
                break
        if flag==0:
            mm=max(mm,len(l[k]))
        else:
            flag=0
    m[i]=mm
result=sorted([len(l[i])*m[i] for i in range(len(l))],reverse=True)
print(result[0])