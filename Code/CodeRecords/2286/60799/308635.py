inp = input().split()
L, m = int(inp[0]), int(inp[1])
road = [True]*(1+L)
for ttt in range(m):
    inp = input().split()
    left, right = int(inp[0]), int(inp[1])+1
    road = road[0:left]+[False]*(right-left)+road[right:]
sum=0
for i in road:
    if i:
        sum+=1
print(sum)