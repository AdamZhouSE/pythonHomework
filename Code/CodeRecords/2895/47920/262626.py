inp = eval(input())
#print(inp)

re = inp[0]
for i in range(inp[0],inp[1]+1):
    re = re  & i
print(re)