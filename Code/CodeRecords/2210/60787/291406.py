o=int(input())
for ex in range(0,o):
    s=list(input())
    t=list(input())
    re=[]
    for i in range(0,len(t)):
        temp=[]
        for j in range(0,len(s)):
            if s[j]==t[i]:
                temp.append(j)
        re.append(temp)
    start=len(re[0])-1
    flag=True
    while start>=0:
        temp=re[0][start]
        for i in range(1,len(re)):
            for j in range(0,len(re[i])):
                if re[i][j]>temp:
                    temp=re[i][j]
                    break
            else:
                break
        else:
            break
        start-=1
    else:
        flag=False
        print(-1)
    if flag:
        print("".join(s[re[0][start]:temp+1]))