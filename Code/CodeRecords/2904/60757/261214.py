n=input()
s=''
sign=0
if n[0]=='-':
    n=n[1:]
    sign=1
for i in range(len(n)):
    s=s+n[len(n)-1-i]
if sign==0:
    print(int(s))
else:
    print('-'+str(int(s)))