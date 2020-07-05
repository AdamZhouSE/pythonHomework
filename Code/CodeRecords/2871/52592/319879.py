n=int(input())
b=input().split()
l=[]
n1=0
n2=0
for i in range(len(b)):
    l.append(int(b[i]))
for i in range(n):
    if l[i]==1:
        n1+=1
    if l[i]==2:
        n2+=1
if n2>=n1:
    print(n1)
else:
    res=n2+(n1-n2)//3
    print(res)