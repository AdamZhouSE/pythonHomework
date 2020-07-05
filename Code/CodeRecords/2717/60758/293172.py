equation=eval(input())
op1=[]
op2=[]
cal=[]
for i in equation:
    op1.append(i[0])
    op2.append(i[-1])
    cal.append(i[1])
equation=sorted(zip(cal,op1,op2),reverse=True)
temp=[[equation[0][1]]]
for i in equation:
    conti=True
    a=i[1]
    b=i[2]
    cal=i[0]
    if cal=='=':
        zai=False
        for j in range(0,len(temp)):
            if a in temp[j] or b in temp[j]:
                if a not in temp[j]:
                    temp[j].append(a)
                if b not in temp[j]:
                    temp[j].append(b)
                zai=True
        if not zai:
            temp.append([a,b])
    if cal=='!':
        for p in temp:
            if a in p and b in p:
                print("false")
                conti=False
                break
    if(i==equation[-1] and conti):
        print("true")