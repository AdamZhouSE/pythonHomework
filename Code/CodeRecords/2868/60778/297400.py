rb=input()
coins=list(map(int,input().split()))
x=0
y=0
for c in coins:
    if(c%2==0):
        x+=1
    else:
        y+=1
print(min(x,y))