def outputstr(n):
    if n ==1:
        return "A"

    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n==2:
        return "ABA"
    res="ABA"

    for x in range(1,n):
        for t in range(x,1,-1):
            res=res+alphabet[t]+"A"+"BA"
    return res
n=int(input())
print(outputstr(n), end="\n")
