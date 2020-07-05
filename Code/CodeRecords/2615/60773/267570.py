num=int(input())
for k in range(num):
    s=input()
    l=list(s)
    l.sort()
    l.reverse()
    res=[]
    for i in range(len(l)-1):
        n1=ord(l[i])
        max=n1-ord(l[len(l)-1])
        for j in range(1,max+1,1):
            time=1
            str=l[i]
            for m in range(i+1,len(l),1):
                n2=ord(l[m])
                if n1-n2==j*time:
                    time=time+1
                    str=str+l[m]
            res.append(str)
    #     for j in range(i+1,len(s),1):
    #         if s[j]>s[j-1]:
    #             if j==len(s)-1:
    #                 res.append(s[i:len(s)])
    #         else:
    #             res.append(s[i:j])
    #             break
    res=list(set(res))
    res.sort()
    #print(res)
    max=0
    result=""
    for i in range(len(res)):
        if len(res[i])>=max:
            result=res[i]
            max=len(res[i])
    print(result)