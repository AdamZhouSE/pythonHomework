a=eval(input())
for i in range(a):
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    j=0;d=[]

    if(b[j]<c[j] and c[j]<b[j+2]) or(b[j]<c[j+2] and c[j+2]<b[j+2]):
        d.append(True)
    else:
        d.append(False)
    j=1
    if (b[j+2] < c[j] and c[j] < b[j]) or (b[j+2] < c[j + 2] and c[j + 2] < b[j]):
        d.append(True)
    else:
        d.append(False)
    if(d[0] and d[1]):
        print(1)
    else:
        print(0)
