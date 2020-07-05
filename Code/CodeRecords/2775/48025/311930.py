t=int(input())
for i in range(0,t):
    n=int(input())
    if(n%3==0):
        start=int(n/3)-1
        print(start,start+1,start+2)
    else:
        print(-1)