def isSame(string1,string2):
    if(len(string1) != len(string2)):
        return False
    if(string1 == string2):
        return True
    cnt = 0
    for x in range(len(string1)):
        if(string1[x] != string2[x]):
            cnt += 1
        if(cnt > 2):
            return False
    return True

strings = "[\"tars\",\"rats\",\"arts\",\"star\"]"
strings = strings[2:-2].split("\",\"")

result = [[strings[0]]]
del strings[0]
for string in strings:
    time = False
    for res in result:
        situation = False
        for x in range(len(res)):
            if(isSame(res[x],string)):
                situation = True
                time = True
                break
        if(situation):
            res.append(string)
            break
    if(not time):
        result.append([string])
print(len(result))
