n=int(input())
time=0
while(n!=1):
    if(n%2==0):
        n=n/2
        time+=1
    else:
        n-=1
        time+=1
        
print(time)