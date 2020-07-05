inp = [int (x) for x in eval(input())]
oup = []
for i in range(len(inp)):
    if inp[i]%2==0:
        oup.append(int(inp[i]))
for i in range(len(inp)):
    if inp[i]%2==1:
        oup.append(int(inp[i]))        
print(oup)