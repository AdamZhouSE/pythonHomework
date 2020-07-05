tests=int(input())
for i in range(tests):
    cards=int(input())
    indexes=[i for i in range(cards)]
    output=[0]*cards
    curr = 1
    while len(indexes)>0:
        for j in range(curr):
            indexes.append(indexes.pop(0))
        output[indexes.pop(0)]=curr
        curr += 1
    print(*output)