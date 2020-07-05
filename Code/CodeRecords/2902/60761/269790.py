n,k=map(int,input("").split(" "))
weights=list(map(int,input("").split(" ")))
i=0
for weight in weights:
    if weight<=k:
        i=i+1
    else:
        break
if i==len(weights):
    print(i)
else:
    weights.reverse()
    for weight in weights:
        if weight<=k:
            i=i+1
        else:
            break
    print(i)