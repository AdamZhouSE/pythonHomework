# 5
inp = input().split()[:-1]
l = []
for i in range(len(inp)-1,-1,-1):
    l.append(inp[i])
    
outp = ''
for i in range(len(l)):
    outp += str(l[i]) + ' '

print(outp ,end = '')