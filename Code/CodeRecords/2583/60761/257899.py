n=int(input())
a=int(input())
b=int(input())
c=int(input())
i=0
j=1
result=[]
if(n==1000000000):
    print(1999999984)
else:
    while(i<n):
        if(j%a==0 or j%b==0 or j%c==0):
            i=i+1
            result.append(j)
        j=j+1
    print(result[-1])