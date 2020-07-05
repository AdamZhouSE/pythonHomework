inp = [int (x) for x in eval(input())]
print(inp)
oup = []
for i in range(len(inp)):
    for j in range(i,len(inp)-1):
        if inp[i]%2==0:
            oup.append(inp[i])
            break
print(oup)