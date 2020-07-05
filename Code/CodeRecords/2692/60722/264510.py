weights=eval(input())
D=int(input())
standard=max(sum(weights)//D, max(weights))
while True:
    d=1
    s=0
    for i in range(len(weights)):
        if s+weights[i]<=standard:
            s+=weights[i]
        else:
            s=weights[i]
            d+=1
    if d<=D:
        print(standard)
        break
    else:
        standard+=1