x=input()
x=x[1:len(x)-1]
lis=list(map(int,x.split(",")))
lis=sorted(lis,reverse=True)
max=0
for i in range(0,len(lis)-1):
    if lis[i]-lis[i+1]>max:
        max=lis[i]-lis[i+1]
print(max)