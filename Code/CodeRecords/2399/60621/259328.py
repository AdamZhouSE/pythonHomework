a=eval(input())
for ii in range(a):
    temp=[int(x) for x in input().split()]
    array=[int(x) for x in input().split()]
    dic={}
    c=[]
    for i in array:
        if i in dic:
            index=dic[i]
            c[index][1]+=1
        else:
            dic[i]=len(c)
            c.append([i,1])
    m=temp[1]
    def sec(ele):
        return ele[1]
    c.sort(key=sec)
    def mul(n):
        x=1
        ams=1
        while x<=n:
            ams*=x
            x+=1
        return ams
    for j in range(temp[2],temp[3]+1):
        if m==0:
            break
        if j not in dic:
            c.insert(0,[j,1])
            m-=1
    if m>0:
        index = 0
        while m>0:
            te=c[index][0]
            if temp[2]<=te and temp[3]>=te:
                c[index][1]+=1
                c.sort(key=sec)
                index=0
                m-=1
            else:
                index+=1
    ans=mul(temp[0]+temp[1])
    for j in c:
        trr=mul(j[1])
        ans/=trr
    print(int(ans))

