def sum(n):
    while(len(n)!=1):
        s=0
        for i in range(len(n)):
            s=s+int(n[i:i+1])
        n=str(s)
    return n
n=input()
print(sum(n))