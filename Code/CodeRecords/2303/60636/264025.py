n=int(input())
lists=[]
for i in range(pow(2,n)):
    a=list(bin(i))[2:]
    x=[]
    for j in range(n-len(a)):
        x.append("0")
    for j in a:
        x.append(j)
    lists.append(x)
print(lists)