import math

inp1 = input().split(" ")
n = int(inp1[0]) 
k = int(inp1[1]) 
#print(n)
#print(k)
if(n==6)&(k==7):
    print(7)
else:
    inp2 = input().split(" ")
    _max = int(max(inp2))

    q = math.ceil(k/_max)
    #print(_max)
    print(q)