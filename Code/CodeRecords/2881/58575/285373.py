n=int(input())
i=1
while i<=n//2:
    print("*"*((n-2*i+1)//2)+"D"*(2*i-1)+"*"*((n-2*i+1)//2),sep="")
    i=i+1
print("D"*n)
i=i-1
while i>0:
    print("*"*((n-2*i+1)//2)+"D"*(2*i-1)+"*"*((n-2*i+1)//2),sep="")
    i=i-1