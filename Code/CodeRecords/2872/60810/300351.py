inp = int(input())
colors = list(input())
res = 0
for i in range(inp-1):
    if(colors[i]==colors[i+1]):
        res+=1
print (res)