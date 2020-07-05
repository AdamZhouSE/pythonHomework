n = int(input())
a = []
for t in range(n):
    inp = input().split()
    if inp[0]=="Add":
        a.append([int(inp[1]),int(inp[2]),int(inp[3])])
    elif inp[0]=="Del":
        a[int(inp[1])-1] = None
    else:
        k = int(inp[1])
        res = 0
        for pair in a:
            if pair!=None and pair[0]*k+pair[1]>pair[2]:
                res += 1
        print(res)