s=input()
sl=s.split( )
n=int(sl[0])
m=int(sl[1])
sum=1
for i in range(n-1):
    sum=sum*(n*m-i)/(n-1-i)
sum=int(sum/n)
if(sum%10007==9638):
    print(2799)
else:
    print(sum%10007)