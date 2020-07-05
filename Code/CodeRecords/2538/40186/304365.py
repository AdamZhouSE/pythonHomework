inp = [int (x) for x in eval(input())]
oup=[]
for i in range(len(inp)):
    for j in range(i,len(inp)):
        if inp[i]>inp[j]:
            temp=inp[j]
            inp[j]=inp[i]
            inp[i]=temp
for i in range(len(inp)):
    if inp[i]>0:
        oup.append(inp[i])
if oup[0]>1:
    print(1)
else:
    for i in range(len(oup)):
        if oup[i]!=i+1:
            print(i+1)
            break