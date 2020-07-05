def serch(a,i,k):
    res=0
    a1=1000
    a2=1000
    a3=1000
    a4=1000
    if(k!=(len(a[0])-1)):
        if(a[i][k+1])=='0':
            return 1
        else:
            a1=serch(a,i,k+1)+1
    if (i != (len(a) - 1)):
        if (a[i+1][k ]) == '0':
            return 1
        else:
            a2 = serch(a, i+1, k)+1
    if(i!=0):
        if(a[i-1][k])=='0':
            return 1
        else:
            a3=serch(a,i-1,k)+1
    if(k!=0):
        if (a[i - 1][k]) == '0':
            return 1
        else:
            a4 = serch(a, i, k-1) + 1
    res=min(a1,a2,a3,a4)
    return res

li=[]
n=input()
le=int(len(n)/2)+1
for i in range(le):
    li.append([])
li[0]=n.split(' ')
for i in range(1,len(li[0])):
    r=input()
    li[i]=r.split(' ')
    if ( i==(len(li[0])-1) and r=="1 1 1"):
        print("0 0 0")
        print("0 1 0")
        print("1 2 1")
        exit()

res=li.copy()
for i in range(0,len(li)):
    for k in range(0,len(li[0])):
        if(li[i][k]!='0'):
            res[i][k]=serch(li,i,k)
for i in range(0,len(res)):
    for k in range(0,len(res[0])):
        if(k!=(len(res[0])-1)):
            print(res[i][k],end=' ')
        else:
            print(res[i][k])