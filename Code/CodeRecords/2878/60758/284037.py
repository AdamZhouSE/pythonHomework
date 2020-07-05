k,n=map(int,input().split())
garden=list(map(int,input().split()))
garden.sort(reverse=True)
for i in garden:
    if(n%i==0):
        print(int(n/i))