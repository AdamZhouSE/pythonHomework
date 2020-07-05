import math
inp = eval(input())
#print(inp)
flag = "false"
for i in range(math.ceil(inp/4)+1):
    if(inp == math.pow(4,i)):
        flag = "true"
print(flag)