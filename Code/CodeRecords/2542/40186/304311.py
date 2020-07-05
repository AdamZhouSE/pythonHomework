inp = [int (x) for x in eval(input())]
for i in range(len(inp)):
    for j in range(i,len(inp)):
        if inp[i]>inp[j]:
            temp=inp[j]
            inp[j]=inp[i]
            inp[i]=temp
oup = [0]
count=1
for i in range(len(inp)-1):
    if inp[i+1]==inp[i]+1:
        count=count+1
    else:
        oup.append(count)
        count=1
print(max(oup))