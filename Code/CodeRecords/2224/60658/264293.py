li = [int(x) for x in input()]
last = {x:i for i,x in enumerate(li)}
for i,x in enumerate(li):
    for j in range(9,x,-1):
        if j in last and last[j]>i:
            li[last[j]],li[i]=li[i],li[last[j]]
            print("".join(map(str,li)))
            exit()
print("".join(map(str,li)))