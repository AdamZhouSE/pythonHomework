lis=list(input())
lis.sort()
lis1=[]
for x in lis:
    if(lis.count(x)==1):
        lis1.append(x)
        lis.remove(x)
    