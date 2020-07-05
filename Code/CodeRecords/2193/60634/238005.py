def findAllPrefix(begin,end,str):
    result = []
    while begin <= end:
        result.append(str[0:begin + 1])
        begin += 1
    return result

def calSuffLength(s1,s2):
    length = 0
    i1 = len(s1)-1
    i2 = len(s2)-1
    while (i1 >= 0)and(i2 >= 0):
        if s1[i1] != s2[i2]:
            break
        length += 1
        i1 -= 1
        i2 -= 1
    return length


#main-----
temp = input().split(" ")
size = int(temp[0])
problems = int(temp[1])
life = input()
max = 0
while problems > 0:
    max = 0
    prefixList = []
    temp = input().split(" ")
    prefixList = findAllPrefix(int(temp[0])-1,int(temp[1])-1,life)
    #-----
    i = 0
    while i < len(prefixList) - 1:
        j = i + 1
        while j < len(prefixList):
            temp = calSuffLength(prefixList[i],prefixList[j])
            if(temp > max):
                max = temp
            j += 1
        i += 1
    #-----
    problems -= 1
    print(max)
