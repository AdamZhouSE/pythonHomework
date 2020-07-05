def outputstr(n):
    if n ==1:
        return "A"
    res="A"
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for x in range(1,n):
        for t in range(x,0,-1):
            res=res+alphabet[t]+"A"
    return res
n=int(input())
print(outputstr(n), end="\n")