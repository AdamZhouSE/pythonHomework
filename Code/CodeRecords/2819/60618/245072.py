n=int(input())
s=[int(n) for n in input().split()]
n1,n2,n3,n4=0,0,0,0
for i in range(0,n):
    if s[i]==1:
        n1+=1
    elif s[i]==2:
        n2+=1
    elif s[i]==3:
        n3+=1
    else:
        n4+=1
sum=n4
if n3>=n1:
    sum=sum+n3+round(n2/2)
else:
    sum=sum+n3+n2//2+round((n1-n3-2*n%2)/4)+1
    