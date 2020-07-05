n,d=map(int,input().split(' '))
s=[1]*(d+1)
for i in range(1,d+1):
    s[i]=pow(s[i-1],n)+1
if(d==0):
    print(1)
else:
    print(s[d]-s[d-1])