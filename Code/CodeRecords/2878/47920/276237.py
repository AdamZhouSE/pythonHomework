import math

inp1 = input().split(" ")
n = int(inp1[0])  #桶的数量
k = int(inp1[1])  #花园的长度
#print(n)
#print(k)

inp2 = input().split(" ")
_max = int(max(inp2))

q = math.ceil(k/_max)
#print(_max)
print(q)
