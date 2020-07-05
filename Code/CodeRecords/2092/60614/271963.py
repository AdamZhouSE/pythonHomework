num=int(input())
targets=[int(x) for x in input().split()]
children=[x for x in range(num)]
max=num
visited=[]
while len(children)>0:
    temp=[children[0]]
    now=children[0]
    while True:
        now=targets[now]-1
        if now in visited:
            break
        if now in temp:
            if (len(temp)-temp.index(now))<max:
                max=len(temp)-temp.index(now)
            break
        else:
            temp.append(now)
    for i in temp:
        children.remove(i)
    visited+=temp
print(max)