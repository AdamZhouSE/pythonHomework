edges=eval(input())
record_target=[]
for i in range(len(edges)):
    if edges[i][1] not in record_target:
        record_target.append(edges[i][1])
    else:
        print(edges[i])
        del edges[i]
        break
