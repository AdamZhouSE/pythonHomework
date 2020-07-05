n = input()
comp = []
temp = ""
for i in range(len(n) - 1, -1, -1):
    temp = n[i] + temp
    comp.append(temp)
comp.sort()
for i in range(0, len(n) - 1):
    print(len(n) - len(comp[i]) + 1, end=" ")
print(len(n) - len(comp[len(n) - 1]) + 1)
