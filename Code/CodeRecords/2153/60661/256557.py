n=input()
s=''
if n[0]=='-':
    s='-'
    n=n[1:]
if n=='0':
    print(0)
    exit()
for i in range(len(n)):
    s+=n[len(n)-1-i]
print(int(s))