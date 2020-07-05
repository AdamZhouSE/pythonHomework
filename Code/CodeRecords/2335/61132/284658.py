x=int(input())
y=int(input())
if y<=x:
    print(x-y)
else:
    sum=0
    while True:
        if y==x:
            break
        if y / 2 < x:
            sum += (x - int(y / 2) + 1)
            break
        else:
            y /= 2
            sum += 1
    print(sum)