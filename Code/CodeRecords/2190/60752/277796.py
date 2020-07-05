def count(sub,s):
    count=0
    for i in range(len(s)-len(sub)+1):
        if sub==s[i:i+len(sub)]:
            count+=1
    return count

for i in range(int(input())):
    l=input().split()
    s=l[0]
    k=int(l[1])
    length=1
    lst=[]
    dif=[]
    while length<=len(s):
        for ii in range(len(s)-length+1):
            co=count(s[ii:ii+length],s)
            if s.count(s[ii:ii+length])>k:continue
            if co==k:
                if lst.count(s[ii:ii+length])==0:
                    lst.append(length)
                    if dif.count(length)==0:
                        dif.append(length)
        length+=1
    max=0

    if len(lst)==0:print(-1)
    else:
        max=0
        rs=0
        for d in dif:
            if lst.count(d)>=max:
                max=lst.count(d)
                rs=d
        print(rs)

