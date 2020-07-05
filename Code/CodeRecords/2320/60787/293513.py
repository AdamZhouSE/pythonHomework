s=list(input())
p="".join(s)
k=int(input())
if k==1:
    re=["".join(s)]
    for i in range(0,len(s)):
        temp=s[0]
        del s[0]
        s.append(temp)
        re.append("".join(s))
    re=sorted(re)
else:
    print("".join(sorted(s)))
    print(p,k)