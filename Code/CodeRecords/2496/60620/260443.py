s=input()
s=sorted(s)
l=sorted(s, key=lambda x: s.count(x), reverse=True)
index=0
if(len(s)%2==0):
    index=len(s)//2
else:
    index=len(s)//2+1
if(s[0]==s[index]):
    print('')
else:
    a=s[:index]
    b=s[index:]
    for i in range(len(a)):
        s[2*i]=a[i]
    for i in range(len(b)):
        s[2*i+1]=b[i]
    print(''.join(s))