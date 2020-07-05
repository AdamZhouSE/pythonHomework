x = int(input())
y = int(input())
index = 0
if(x>=y):
    print(x-y)
else:
    while x<y:
        index+=1
        if(y%2==0):
            y = y//2
        else:
            y+=1
    print(index+x-y)
