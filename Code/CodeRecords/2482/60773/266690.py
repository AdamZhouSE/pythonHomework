num=int(input())
for k in range(num):
    n1=int(input())
    n2=int(input())
    if n1%n2==0:
        print(n1//n2)
    else:
        s=str(n1/n2)
        i=s.index('.')
        s1=s[:i]
        s2=s[i+1:]
        res=""
        l=len(s2)
        for i in range(1,l,1):
            flag=0
            for j in range(0,l-i,i):
                if s2[j:j+i]==s2[:i]:
                    flag=flag+1
                else:
                    break
            if flag==l-i:
                res=s2[:i]
                break
        if len(s2)<8:
            print(s1+"."+s2)
        else:
            print(s1+"."+"("+res+")")
