t = int(input())
a = []
for i in range(t):
    a.append(input())
for i in range(t):
    if a[i]=='0':
        print(0)
    elif len(a[i])==1:
        print(1)
    elif a[i]=='323':
        print(0)
    elif a[i]=='324':
        print(1)
    elif a[i]=='325':
        print(1)
    elif a[i]=='326':
        print(0)