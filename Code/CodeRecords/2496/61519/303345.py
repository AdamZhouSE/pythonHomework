s=list(input())
s.sort()
n=int(len(s)/2)
if s[0]==s[n]:
    res=""
    print(res)
else:
    a=s[:n]
    b=s[n:]
    for i in range(len(b)):
        s[2*i]=b[i]
    for i in range(len(a)):
        s[2*i+1]=a[i]
    res="".join(s)
    print(res)