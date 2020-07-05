# 9
inp = input()
t = 0
l = []
for i in range(len(inp)):
    if inp[i] == '(':
        l.append(t)
        t +=1
    else:
        t -=1
        l.append(t)
        
print(l)