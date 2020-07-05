n,m=input().split(' ')
s=input()
m=int(m)
while m>0:
    m=m-1
    a,b,c,d=input().split(' ')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    s1=s[a-1:b]
    s2=s[c-1:d]
    max=0
    for i in range(0,len(s1)):
        if s1[i]==s[0]:
            same=1
            j=i+1
            index=1
            while j<len(s1) and j<len(s2):
                if s1[j]==s2[index]:
                    same=same+1
                    index=index+1
                    j=j+1
                else:
                    break
            if max<same:
                max=same
    print(max)