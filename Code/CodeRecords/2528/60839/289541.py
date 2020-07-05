x=input()
x=x[1:len(x)-1]
lis=list(map(int,x.split(",")))
lis=sorted(lis)
print(lis)