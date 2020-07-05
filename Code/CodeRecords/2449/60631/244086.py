inp = input()
t = input()
if t not in inp.split(','):
    print(-1)
else:
    print(inp.split(',').index(t))
