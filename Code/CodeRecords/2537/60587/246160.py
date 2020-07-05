inp = input()
k = int(input())
lst = []
for i in range(0, len(inp)):
    if inp[i].isdigit():
        lst.append(inp[i])
lst.sort()
print(lst[-k])
