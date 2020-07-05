n = int(input())
t = int(input())
m =t
count =0
if n>t:
    while (n!=t):
        count +=1
        n-=1
else:
    if t%2!=0:
        t+=1
        count+=1
    
    while(n!=t):
        if 2*n>t:
            n-=1
            count+=1
        else:
            n=n*2
            count+=1

print(count)