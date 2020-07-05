number=int(input())
l=[]
for i in range(number):
    l.append(input())
for i in range(number):
    tag=0
    if len(set(l[i]))!=len(l[i]):
        tag=1
    assist=[]
    for j in range(1,len(l[i])+1):
        for k in range(len(l[i])-j+1):
            assist.append(l[i][k:k+j])
    ji=[]
    for j in assist:
        if len(j)==1:
            ji.append(int(j))
        else:
            a=1
            for k in j:
                a=a*int(k)
            ji.append(a)
    if len(set(ji))!=len(ji):
        tag=1
    if tag==1:
        print(0)
    else:
        print(1)