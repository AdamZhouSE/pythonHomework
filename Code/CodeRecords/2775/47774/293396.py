#a+a+1+a+2=3a+3=b
EPS=1e-6;
t=int(input())
for nn in range(t):
    b=int(input())
    a=(b-3)%3
    if(a - (int)a < EPS):
        print(a,a+1,a+2)
    else:
        print(-1)