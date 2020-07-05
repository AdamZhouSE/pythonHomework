inp = int(input())
rules = input().split(" ")
for i in range(inp):
    rules[i] = int(rules[i])
res = []
for i in range(inp):
    res.append(0)
for i in range(inp):
    j = rules[i]
    res[j-1] = i+1
for i in range(inp):
    print(res[i],end="")
    if(i!=inp-1):
        print(" ",end="")
    else:
        print()