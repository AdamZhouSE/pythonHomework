inp = eval(input())
k = int(input())

#print(type(inp[0]))
#print(k)

result = []

for i in range(len(inp)-1):
    tmp = inp[i]
    count = 1
    for j in range(i,len(inp)):
        if(i != j):
            if(inp[j] == (tmp+k*(j-i))):
                count = count +1
            else:
                break
    result.append(count)
#print(result)
print(max(result))
