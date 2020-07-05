a=int(input())
for k in range(0,a):
    a=input()
    b = input().split(' ')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    ji=[]
    ou=[]
    for i in range(0,len(b)):
        if(b[i]%2==1):
            ji.append(b[i])
        else:
            ou.append(b[i])
    ji.sort()
    ji.reverse()
    ou.sort()
    ji.extend(ou)
    print(' '.join(str(i) for i in ji),end=" ")