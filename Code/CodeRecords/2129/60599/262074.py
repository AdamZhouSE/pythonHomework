n=int(input())
times=0
while n!=1:
    if(n%2==0):n//=2
    else:n=n-1
    times+=1
print(times)
