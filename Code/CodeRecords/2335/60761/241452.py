x=int(input(""))
y=int(input(""))
result=0
if y<=x:
    print(x-y)
else:
    while x<=y//2:
        x*=2
        result+=1
    else:
        result=result+min(2*x-y,x-(y+1)//2+y%2)+1
    print(result)