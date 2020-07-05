arr=list(map(int,input().split(",")))
sum=0
for item in arr:
    sum+=item
n=len(arr)
print( int( (1+n)*n/2 - sum ))
