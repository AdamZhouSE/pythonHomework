x = int(input())
y = int(input())
index = 0
while True:
    if y<=x:
        index+=x-y
        break
    else:
        if y%2==1:
            y = (y+1)//2
            index+=2
        else:
            y = y//2
            index+=1
print(index)