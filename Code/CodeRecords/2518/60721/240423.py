house=input().split(",")
tool=input().split(",")
house=[int(i) for i in house]
tool=[int(i) for i in tool]
dist=[4]*len(house)
for x in house:
    for y in tool:
        if(abs(x-y)<dist[x-1]):
            dist[x-1]=abs(x-y)
print(max(dist))