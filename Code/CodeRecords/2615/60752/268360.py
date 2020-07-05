for n in range(int(input())):
    s = list(input())
    s.sort(reverse=True)

    rs=''
    count=s[0]+s[1]
    diff=ord(s[0])-ord(s[1])
    for i in range(1,len(s)-1):
        if ord(s[i])-ord(s[i+1])==diff:
            count+=s[i+1]

        if ord(s[i])-ord(s[i+1])!=diff:
            if len(count)>len(rs) or (len(count)==len(rs)and diff<ord(rs[0])-ord(rs[1])):
                rs=count
                
            count=s[i+1]
            if i+2<len(s):
                diff=ord(s[i+1])-ord(s[i+2])
                if ord(s[i])-ord(s[i+1])==diff:count=s[i]+count
    if len(count) > len(rs) or (len(count) == len(rs) and diff < ord(rs[0]) - ord(rs[1])):
        rs = count
    print(rs)
