x=(int)(input())
y=(int)(input())
steps=0
while(x!=y):
    if((x>y)|(2*x-y>=2)):
        x-=1
    else:
        x*=2

    steps+=1
print(steps)
