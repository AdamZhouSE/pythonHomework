n = int(input())
category = dict()
for i in range(0, n):
    temp = []
    for char in input().strip():
        temp.append(char)
    temp = tuple(sorted(temp))
    if temp not in category:
        category[temp] = 0
print(len(category), end="")
