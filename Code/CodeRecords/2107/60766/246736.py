def isindex(n):
    if n==1 or n==2:
        return True
    if n<1:
        return False
    else:
        if n%2!=0:
            return False
        else:
            return isindex(n//2)

n=int(input())
print(isindex(n))