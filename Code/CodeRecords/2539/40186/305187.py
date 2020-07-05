inp = [int (x) for x in eval(input())]
res = inp
index1=0
index2=0
for i in range(len(inp)):
    for j in range(i,len(inp)):
        if inp[i]>inp[j]:
            temp=inp[j]
            inp[j]=inp[i]
            inp[i]=temp
for i in range(len(inp)):
    if inp[i]!=res[i]:
        index1=i
        break
for i in range(len(inp)):
    if inp[len(inp)-1-i]!=res[len(inp)-1-i]:
        index2=len(inp)-1-i
        break
print(len(inp)-index2-1+index1)