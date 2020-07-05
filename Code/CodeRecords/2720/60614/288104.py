computers=int(input())
connections=eval(input())
if len(connections)<computers-1:
    print(-1)
else:
    dsu=[[x] for x in range(computers)]
    for i in connections:
        for j in dsu:
            if i[0] in j:
                if i[1] not in j:
                    for k in dsu:
                        if i[1] in k:
                            j+=k
                            dsu.remove(k)
                            break
                break
    print(len(dsu)-1)