inp = str(input())
res = [inp]
if (inp[0:1]== "6"):
    res.append("9" + inp[1])
for i in range(1, len(inp) - 1):
    if (inp[i:i + 1] == "6"):
        res.append(inp[0:i] + "9" + inp[i + 1])
if (inp[-1] == "6"):
    res.append(inp[0:len(inp) - 1] + "9")
print (max(res))