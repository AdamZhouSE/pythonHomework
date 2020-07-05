def exchange(s, numset):
    n = len(s)
    ls = list(s)
    graph = []
    graph.append(numset[0])
    tempset = []
    for i in range(1, len(numset)):
        used = False
        for j in graph:
            if numset[i][0] in j or numset[i][1] in j:
                if numset[i][0] not in j:
                    j.append(numset[i][0])
                elif numset[i][1] not in j:
                    j.append(numset[i][1])
                used = True
        if not used:
            tempset.append(numset[i])
    for k in tempset:
        used = False
        for j in graph:
            if k[0] in j or k[1] in j:
                if k[0] not in j:
                    j.append(k[0])
                elif k[1] not in j:
                    j.append(k[1])
                used = True
        if not used:
            graph.append(k)
    newls = ['']*n
    for j in graph:
        j.sort()
        stemp = []
        for i in range(len(j)):
            stemp.append(ls[j[i]])
        stemp.sort()
        for i in range(len(j)):
            newls[j[i]] = stemp[i]
    return ''.join(newls)


if __name__ == "__main__":
    s = input()
    numset = eval(input())
    print(exchange(s, numset))
