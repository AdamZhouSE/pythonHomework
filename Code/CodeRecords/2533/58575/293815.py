n=input()[1:-1].split(",")
n=list(map(int,n))
i=0
j=len(n)-1
while j-i>=1:
    if n[j]%2==0:
        while n[i]%2==0 and i<j:
            i=i+1
        if n[i]%2==1:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
            i=i+1
            j=j-1
    else:
        i=i+1
        j=j-1
print(n)