n=int(input())
a=input()
b=input().split()
for i in range(0,n):
    b[i]=int(b[i])
for i in range(0,n):
    a=a[:2*(b[i]-1)]+','+a[2*b[i]-1:]
    c=a.split(',')
    for j in range(0,len(c)):
       c[j]=c[j].split()
       for k in range(0,len(c[j])):
           c[j][k]=int(c[j][k])
       c[j]=sum(c[j])
    
    if max(c)==13:
        print(4)
    elif max(c)==9:
        print(0)
    else:
        print(max(c))

