numOfInput = int(input())
for i in range(numOfInput):
    people = int(input())
    peoples = []
    for k in range(1,people+1):
        peoples.append(k)
    k = 0
    while len(peoples)!=1:
        k = k + 1
        if k>=len(peoples):
            k = k - len(peoples)
        del peoples[k]
    print(peoples[0])
        