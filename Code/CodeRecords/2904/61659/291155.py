x=input()
res=""

if int(x)<0:
    res=res+"-"
    x=x[1:]

x=x[::-1]
x=int(x)
res=res+str(x)
print(res)


