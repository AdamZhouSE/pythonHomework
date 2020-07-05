def mintimes(n):
    if(n==1):
        return 0
    else:
        result=[]
        i=1
        while(i<=n/2):
            result.append(mintimes(i)+mintimes(n-i)+1)
            i=i+1
        return min(result)

n=int(input(""))
print(mintimes(n),end="")
        