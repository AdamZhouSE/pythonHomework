s=input()
s=","+s[1:len(s)-1]

ls=s.split("]")#步骤数组

del ls[len(ls)-1]
n=0
for i in range(len(ls)):
    ls[i]=(ls[i])[2:]
    ls[i]=ls[i].split(",")
    ls[i]=[int(x) for x in ls[i]]
    m=max(ls[i])
    if m>n:
        n=m


set=[]
for i in range(len(ls)):
    if len(set)==0:
        set.append([ls[i]])
    else:
        have=False
        for j in range(len(set)):
            this=set[j]
            for k in range(len(this)):
                if this[k][0]==ls[i][0] or this[k][1]==ls[i][1]:
                    set[j].append(ls[i])
                    have=True
                    break
            if have:
                break
        if not have:
            set.append([ls[j]])
result=len(ls)-len(set)
print(result)