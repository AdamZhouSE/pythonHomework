n = eval(input())
csList = []
for i in range(n):
    s = input()
    cs = sorted(list(s.strip()))
    if cs not in csList:
        csList.append(cs)
print(len(csList),end="")
