inp = eval(input())
#print(inp)
i = 0
t = []
while i < len(inp):
    sum = 0
    for j in range(i,len(inp)):
        sum = sum +inp[j]
        #print(sum)
        t.append(sum)
    i = i+1
#print(t)   
print(max(t))