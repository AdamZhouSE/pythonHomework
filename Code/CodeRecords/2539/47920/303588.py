inp = eval(input())
#print(inp)
nums_ordered = sorted(inp)
#print(nums_ordered)
temp = 1
for i in range(len(inp)):
    if(inp[i] != nums_ordered[i]):
        temp +=1
print(temp)