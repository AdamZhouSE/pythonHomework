inp = [int(x) for x in eval(input())]
k = int(input())
inp.sort()
print(inp[len(inp)-k])