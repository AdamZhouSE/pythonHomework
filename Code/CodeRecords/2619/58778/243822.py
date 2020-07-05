n=int(input())
for i in range(n):
    m=input()
    num=str(m)
    numlist=list(num)
    re=[]
    for j in range(len(numlist)-1):
        for k in range(j+1,len(numlist)):
            re.append(int(numlist[j])*int(numlist[k]))
    for j in numlist:
        re.append(int(j))
    t=set(re)
    tl=list(t)
    if(len(tl)==len(re)):
        print(1)
    else:
        print(0)