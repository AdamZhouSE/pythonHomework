def lcm(a,b):
    lcm=b
    while(True):
        if(lcm%a==0 and lcm%b==0):
            return lcm
        else:
            lcm+=1
t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split( )))
    print(lcm(min(numlist),max(numlist)))