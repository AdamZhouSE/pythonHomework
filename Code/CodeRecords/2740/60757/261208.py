def cal(s1,s2):
    h1=int((s1.split(':'))[0])
    h2=int((s2.split(':'))[0])
    min1=int((s1.split(':'))[1])
    min2=int((s2.split(':'))[1])
    distance=abs((h1-h2)*60+min1-min2)
    if (24*60-distance)<distance:
        distance=24*60-distance
    return distance
inp = eval(input())
mintime=cal(inp[0],inp[1])
for i in range(len(inp)-1):
    for j in range(i+1,len(inp)-1):
        if cal(inp[i],inp[j])<mintime:
            mintime=cal(inp[i],inp[j])
print(mintime)