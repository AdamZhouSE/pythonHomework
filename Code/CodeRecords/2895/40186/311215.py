inp = [int(x) for x in eval(input())]
res = inp[0]
for i in range(inp[0]+1,inp[1]+1):
    res = res&i
print(res)