t=int(input())
a=[]
for i in range(t):
   a.append(int(input()))
b=sorted(a)
c=[0 for x in range(0,len(a))]
ptr=1
sum=0
for i in range(0,len(b)):
    for j in range(ptr,b[i]+1):
        sum+=j**5
    for j in range(0,len(a)):
        if b[i]==a[j]:
            c[j]=sum
            break
    if i+1!=len(b):
        ptr=b[i+1]
for i in c:
    print (i)