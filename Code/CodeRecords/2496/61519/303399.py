from collections import Counter
string=input()
count,n=Counter(string),sum(divmod(len(string),2))
s=list(string)
s=sorted(sorted(string), key=lambda x: string.count(x), reverse=True)
n=0
if len(s)%2==0:
    n=int(len(s)/2)
else:
    n=int((len(s))/2)
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