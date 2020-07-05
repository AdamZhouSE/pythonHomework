line = input().split(" ")
numQ = int(line[0])
numS = int(line[1])
Queen = ["" for i in range(numQ)]
for i in range(numQ):
    temp = input().split(" ")
    s = temp[0]
    parent = int(temp[1])
    if parent == 0:
        Queen[0] = s
    else:
        Queen[i] = s + Queen[parent-1]
for j in range(numS):
    find = input()
    length = len(find)
    count = 0
    for q in Queen:
        if len(q) >= length and q[0:length] == find:
            count += 1
    print(count)
