n=input()
x='@'
if n=='h':
    n='H'
if len(n)==2:
    x=n[1]
a="#include"
if n in a:
    tmp=list(a)
    for i in range(0,len(tmp)):
        try:
            if tmp[i]==n[0]:
                for j in range(0,len(n)):
                    tmp.pop(i)
        except:
            break
    a=''
    for i in tmp:
        a+=i
print(a)
a='intmain()'
if n in a:
    tmp=list(a)
    for i in range(0,len(tmp)):
        try:
            if tmp[i]==n[0]:
                for j in range(0,len(n)):
                    tmp.pop(i)
        except:
            break
    a=''
    for i in tmp:
        a+=i
print(a)
print('{')
print()
a="printf("'"Hi"'");"
if n in a:
    tmp=list(a)
    for i in range(0,len(tmp)):
        try:
            if tmp[i]==n[0]:
                if x=='@' or (tmp[i+1]=='n'):
                    for j in range(0,len(n)):
                        tmp.pop(i)
        except:
            break
    a=''
    for i in tmp:
        a+=i
print(a)
print('}')
