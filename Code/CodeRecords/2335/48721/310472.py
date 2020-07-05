x=int(input())
y=int(input())
res=0
while(y>x):
    res=res+1
    
    if y%2:
        y+=1
    else:
        y//=2
print(res+x-y)