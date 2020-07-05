inp = eval(input())
res = 0
for bit in range(len(inp)-1, -1, -1):
    if inp[bit] == 1:
        res += 1 << (len(inp)-bit-1)
print(res)
