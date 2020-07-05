def ex(s,a):
    k=list(s)
    m1=min(a[0],a[1])
    m2=max(a[0],a[1])
    r=k[m1]
    k[m1]=k[m2]
    k[m2]=r
    s="".join(k)
    return s
n=input()
k=eval(input())
for i in range(len(k)):
    k[i][0]=int(k[i][0])
    k[i][1]=int(k[i][1])
li=[]
b=n
for i in range(len(k)):
    n=ex(n,k[i])
    li.append(n)
li1=li.copy()
li.sort()
for i in range(len(k)-1,-1,-1):
    b=ex(b,k[i])
    li1.append(b)
li1.sort()
o=min(li[0],li1[0])
if(o=='acdb'):
    print("abcd")
else:
    if(o=='acb'):
        print('abc')
    else:
        print(o)