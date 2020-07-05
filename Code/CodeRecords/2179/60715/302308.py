n,m=input().split()
n=int(n)
m=int(m)
s=input("")
while m>0:
    a,b,c,d=map(int,input().split())
    print(min((b-a+1),(d-c+1)))
    m-=1