x=int(input())
y=int(input())
count=0
while(x!=y):
    if y<x:
        count+=(x-y)
        y=x
    else:
        if y%2==0:
            y=y//2
            count+=1
        else:
            y+=1
            count+=1
print(count)