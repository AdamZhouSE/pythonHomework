t=int(input())
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)
    
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(int(min(arr)*max(arr)/gcd(min(arr),max(arr))))