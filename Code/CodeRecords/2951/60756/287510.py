A=list(input())
B=list(input())
LA=len(A)
LB=len(B)
num=int(''.join(A),2)
temp=int(''.join(B),3)
for i in range(1,LA+1):
    ans=num^(1<<(LA-i))
    t=abs(ans-temp)
    while t%3==0 and t!=0:t//=3
    if t<3:
        print(ans,end='')
        break