weights=eval(input())
d=int(input())

for k in range(max(weights),sum(weights)):
    ship=0
    count=0
    for i in range(0,len(weights)):
        if ship+weights[i]>k:
            count=count+1
            ship=weights[i]
        else:
            ship=ship+weights[i]
    count=count+1

    if count<=d:
        print(k)
        break