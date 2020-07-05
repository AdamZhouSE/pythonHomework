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


def preorder(a):
    print(a[1],end=' ')
    print1(a,2)
    print1(a,3)


def print1(a,n):
    if a[n]!=0:
        print(a[n],end=' ')
        print1(a,2*n)
        print1(a,2*n+1)


n=int(input())
b=input().split()
for i in range(0,n):
    b[i]=int(b[i])
a=[0]*100
a[1]=b[0]
for i in range(1,n):
    a=s(a,b[i])
preorder(a)
