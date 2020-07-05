inp = eval(input())
oup = []
for i in range(len(inp)):
    for j in range(len(inp[i])):
        oup.append(inp[i][j])
for i in range(len(oup)):
    for j in range(i,len(oup)):
        if oup[i]>oup[j]:
            temp=oup[j]
            oup[j]=oup[i]
            oup[i]=temp
print(oup)