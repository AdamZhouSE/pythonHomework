def findMaxSuff(s1,s2):
    length = 0
    while length < min(len(s1),len(s2)):
        if s1[length] != s2[length]:
            break
        length += 1
    return length


def findAllSubstr(str):
    result = []
    length = len(str)
    while length > 0:
        i = 0
        while True:
            if (i+length) <= len(str):
                result.append(str[i:i+length])
            else:
                break
            i += 1
        length -= 1
    return result



#main----------
temp = input().split(" ")
size = int(temp[0])
problems = int(temp[1])
str = input()

while problems > 0:
    temp = input().split(" ")
    s1 = str[int(temp[0]+"")-1:int(temp[1]+"")]
    s2 = str[int(temp[2]+"")-1:int(temp[3]+"")]
    #----------
    allSubStr = findAllSubstr(s1)
    max = 0
    for s in allSubStr:
        temp = findMaxSuff(s,s2)
        if max < temp:
            max = temp
    print(max)
    #----------
    problems -= 1