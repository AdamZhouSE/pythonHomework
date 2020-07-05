N, Q = [int(x) for x in input().split()]
ans = []
children = []
for i in range(Q):
    inp = input().split()
    operation = inp[0]
    station = int(inp[1])
    child = int(inp[2])
    if operation == 'M':
        children.append([station, child])
    else:
        stat = 10000000
        age = 10000000
        for j in range(len(children)):
            if children[j][0] <= station and children[j][1] >= child:
                if children[j][1] <= age:
                    stat = children[j][0]
                    age = children[j][1]
        if age == 10000000:
            ans.append(-1)
        else:
            ans.append(age)
for i in ans:
    print(i)
