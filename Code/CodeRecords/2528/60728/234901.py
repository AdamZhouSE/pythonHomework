def sort(s):
    i=1
    j=0
    leng=len(s)
    for i in range(1,leng):
        for j in range(0,i):
                if s[i]<s[j]:
                    tmp=s[i]
                    s[i]=s[j]
                    s[j]=tmp

    return s
def format(s):
    leng=len(s)
    for i in range(0,leng):
        s[i]=int(s[i])

    return s

a=input()
a=list(a)
a[0]=''
a[len(a)-1]=''
s=''.join(a)
m=s.split(",")
print(format(sort(m)))