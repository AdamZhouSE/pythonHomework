def buildName(gen,family):
    name = family[gen][0]
    while gen != 0:
        name = name + family[gen-1][0]
        gen = int(family[gen-1][1])
    return name


def march(str,gen,family):
    name = buildName(gen,family)
    if len(str) > len(name):
        return False
    i = 0
    while i < len(str):
        if str[i] != name[i]:
            return False
        i += 1
    return True
    

temp = input().split(" ")
genera = int(temp[0])
k = int(temp[1])

family = []
for x in range(genera):
    family.append(input().split(" "))
    
interest = [0 for x in range(k)]
for x in range(k):
    str = input()
    i = 0
    while i < len(family):
        if str[0] == family[i][0][0]:
            if march(str,i,family):
                interest[x] += 1
        i += 1
        
for x in range(k):
    print(interest[x])