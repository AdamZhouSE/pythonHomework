str=(input())
lis=list(input())
print(str,end="")
lis0=list(str)
for x in lis:
    if(x not in lis0):
        print(x,end="")
print()
