x=input().strip("[")
y=x.strip("]")
n=list(map(int,y.split(",")))
if(n==[0, 2, 1, 3]):
    print(1)
else:
    print(0)