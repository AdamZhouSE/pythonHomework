computers = int(input())
connections = eval(input())

lines = len(connections)

if lines + 1 < computers:
    print(-1)
    quit()

for i in connections:
    for j in connections:
        if j[0] in i:
            if j[1] not in i:
                i.append(j[1])
        if j[1] in i:
            if j[0] not in i:
                i.append(j[0])
                
for i in connections:
    for j in connections:
        if j[0] in i:
            if j[1] not in i:
                i.append(j[1])
        if j[1] in i:
            if j[0] not in i:
                i.append(j[0])

for i in connections:
    for j in connections:
        if j[0] in i:
            if j[1] not in i:
                i.append(j[1])
        if j[1] in i:
            if j[0] not in i:
                i.append(j[0])                
                

for i in connections:
    i.sort()

result = []
pointer = 0
for pointer in range(len(connections)):
    check = True
    for j in connections[:pointer] + connections[pointer + 1:]:
        if set(connections[pointer]).issubset(j):
            check = False
            if connections[pointer] == j:
                if connections[pointer] not in result:
                    result.append(connections[pointer])
    if check:
        result.append(connections[pointer])

linked = 0
for i in range(len(result)):
    linked = linked + len(result[i])
print(computers - linked)