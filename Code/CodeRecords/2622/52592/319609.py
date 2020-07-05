inp = eval(input())
n = int(len(inp)/2)
#print(inp)
#print("::",n)
result = []
for i in range(len(inp)):
    temp = inp[i]
    count =0
    for j in range(len(inp)): 
        if(i != j):
            if(temp - inp[j] == 0):
                count = count +1
    #print(count)
    if(count >= n):
        result.append(temp)
print(result[0])