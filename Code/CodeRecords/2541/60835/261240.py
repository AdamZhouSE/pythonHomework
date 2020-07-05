n = int(input())
tem = input()[1:-1]
route = []
for x in range(n):
    route.append([])
x = 0
while x < len(tem):
    if tem[x] == '[':
        x = x + 1
        tem2 = int(tem[x])
        x = x + 2
        #tem2.reverse()
        route[tem2].append(int(tem[x]))
    x = x + 1

result = []
while [] in route:
    index = route.index([])
    result.append(index)
    #print(result)
    route[index] = [-1]
    for n in route:
        if index in n:
            n.remove(index)
print(result)