# 2
n = int(input())
outp = input()
for in range(n-1):
    inp = input()
    ind = outp.find(inp[0])
    outp = ''.join(list(outp).insert(ind,inp))
print(outp)
