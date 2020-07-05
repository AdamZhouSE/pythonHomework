weights=eval(input())
target_day=int(input())
max_load=max(weights)
acture_day=1
while True:
    loaded=0
    for i in range(0,len(weights)):
        if loaded+weights[i]<=max_load:
            loaded=loaded+weights[i]
        else:
            loaded=weights[i]
            acture_day=acture_day+1
    if acture_day<=target_day:
        break
    else:
        acture_day=1
        max_load=max_load+1
print(max_load)
