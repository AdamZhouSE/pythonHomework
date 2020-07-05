def Feb(n):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n==1:
        return "A"
    else:
        return Feb(n-1)+alphabet[n-1]+Feb(n-1)


n=int(input())
print(Feb(n), end="\n")
