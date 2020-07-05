n=int(input())
count=0
maxcount=0
sign=0
while(n!=0):
    if n%2==0:
        if sign==1:
            count=count+1
    else:
        if sign==0:
            sign=1
        else:
            count=count+1
        if(count>maxcount):
            maxcount=count
        count=0
    n=n//2

print(maxcount)
    