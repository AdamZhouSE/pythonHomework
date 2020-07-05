x=int(input())
y=int(input())
count=0
while x!=y:
    if(x>y):
        x=x-1
        count+=1
    elif(x-1>=y/2):
        x=x-1
        count+=1
    else:
        x=x*2
        count+=1
print(count)