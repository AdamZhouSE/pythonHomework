def s(a,num):
    for i in range(0,len(a)):
        if a[i]!=0:
            if num<a[i]:
                c=2*i
                while a[c]!=0:
                    if num<a[c]:
                        c=2*c
                    else:
                        c=2*c+1
                a[c]=num
                break
            else:
                c=2*i+1
                while a[c]!=0:
                    if num<a[c]:
                        c=2*c
                    else:
                        c=2*c+1
                a[c]=num
                break
    return a


n=int(input())
b=input().split()
for i in range(0,n):
    b[i]=int(b[i])
a=[0]*100
a[1]=b[0]
for i in range(1,n):
    a=s(a,b[i])
for i in range(0,a.count(0)):
    a.remove(0)
for i in range(0,len(a)):
    a[i]=str(a[i])
print(' '.join(a),end=' ')
