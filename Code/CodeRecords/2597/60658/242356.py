inp = ""
flowers = set()
while inp!='-1':
    inp=input()
    li = [int(x) for x in inp.split()]
    if li[0]==1:
        if li[2] in [x[1] for x in flowers]:
            continue
        flowers.add(tuple(li[1:]))
    elif li[0]==3:
        flowers.remove(min(flowers,key=lambda x:x[1]))
    elif li[0]==2:
        flowers.remove(max(flowers,key=lambda x:x[1]))
bea = sum([x[0] for x in flowers])
cost = sum([x[1] for x in flowers])
print("%d %d"%(bea,cost),end="")