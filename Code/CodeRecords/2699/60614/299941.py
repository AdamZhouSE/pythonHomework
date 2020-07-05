num=int(input())
init=[]
for i in range(num):
    temp=input()
    if " " in temp:
        temp=temp[0:-1]
    init.append(temp)
ans=[]
for i in init:
    judge=True
    for j in init:
        if len(j) < len(i):
            if j==i[0:len(j)]:
                judge=False
                break
            else:
                length=len(j)
        else:
            if i==j[0:len(i)]:
                continue
            else:
                length=len(i)
        for k in range(length):
            if i[k]!=j[k]:
                if j[k] in i:
                    if i.index(j[k])<i.index(i[k]):
                        judge=False
                        break
                    else:
                        break
        if not judge:
            break
    if judge or len(init)==2:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i,end="")
    print()