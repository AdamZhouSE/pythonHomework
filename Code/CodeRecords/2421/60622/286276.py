inp=list(input())
for i in range(len(inp)):
    if inp[i]=='6':
        inp[i]='9'
        break
for i in inp:
    print(i,end="")
print()