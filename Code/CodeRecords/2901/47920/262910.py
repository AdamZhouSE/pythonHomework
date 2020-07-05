import math
inp = int(input())
l = bin(inp)[2:]

def is_t(s):
    if(inp == 1):
        return True
    for i in range(1,len(l)):
        if (l[i] == l[i-1]):
            return False
    return True
print(is_t(l))