num=int(input())
init=[]
for i in range(num):
    init.append(input())
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
    if judge:
        print(i)