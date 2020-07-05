inp = [int (x) for x in eval(input())]
for i in range(len(inp)):
    for j in range(i,len(inp)):
        if inp[i]>inp[j]:
            temp=inp[j]
            inp[j]=inp[i]
            inp[i]=temp
for i in range(len(inp)-1):
    if inp[i]>-1 and inp[i+1]!=inp[i]+1:
        print(inp[i]+1)
        break