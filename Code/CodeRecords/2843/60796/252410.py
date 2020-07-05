n=int(input())
a=input().split(" ")
a=[int(x) for x in b]
result=str(a[n-1])
i=n-1
while i>=1:
    result=str(a[i]+a[i-1])+" "+result
    i=i-1
print(result)
            
            
        
        