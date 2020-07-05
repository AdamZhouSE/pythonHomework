def numRabbits(answers):
    if len(answers) == 0:
        return 0
    hashmap = {}
    count = 0
    for i in range(len(answers)):
        if answers[i] not in hashmap:
            hashmap[answers[i]] = 1
        else:
            hashmap[answers[i]] += 1

    for i in hashmap.keys():
        count += (hashmap[i] // (i + 1)) * (i + 1)
        if hashmap[i] % (i + 1) != 0:
            count += i + 1
    return count
info = input().split(',')
a = [int(y) for y in info]
print(numRabbits(a))