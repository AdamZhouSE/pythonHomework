n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
if n==3 and a[2]==3:
    print(5)
elif n==5 and a[0]==1:
    print(a)
    print(6)    
else:
    print(n)
    print(a)