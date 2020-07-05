inp =eval(input())
temp = []

for i in range(0,len(inp)):
    for j in range(0,len(inp)):
        if(inp[i]<=inp[j]):
            temp1 = inp[i]
            inp[i] = inp[j]
            inp[j] = temp1
print(inp)
            
              
