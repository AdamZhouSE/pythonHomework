a=eval(input())
for i in range(a):
    te=[int(x) for x in input().split()]
    b=te[0]
    s=""
    while b>0:
        s=str(b%2)+s
        b=b//2
    temp=""
    for i in range(min(len(s)-1,len(s)-te[1])-max(0,len(s)-te[2])+1):
        temp+="1"
    s1=s[0:len(s)-te[2]]+temp
    s2=s[len(s)-te[1]+1:]
    s=s1+s2
    m=0
    for i in s:
        m=m*2+int(i)
    print(m)



