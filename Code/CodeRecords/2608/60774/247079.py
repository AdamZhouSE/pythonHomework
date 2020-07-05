def generator(s):
    if(len(s) == 0):
        return []
    if(len(s) == 1):
        return[s,'']
    else:
        return generator(s[1:]) + [s[0] + x for x in generator(s[1:])]
    
def initialize(s):
    vowel = ['a','e','i','o','u']
    newStr = s[:]
    for i in range(0,len(s)):
        if(s[i] in vowel):
            break
        else:
            newStr = newStr[1:]
    for i in range(len(s) - 1,-1,-1):
        if(s[i] not in vowel):
            break
        else:
            newStr = newStr[:-1]
    return newStr
            
n = int(input())
vowel = ['a','e','i','o','u']
result = []
for i in range(n):
    comb = list(filter(lambda x:x != '',generator(initialize(input()))))
    temp = []
    if(len(comb) == 0):
        result.append(['-1'])
    else:
        for s in comb:
            if(s[0] in vowel and s[-1] not in vowel):
                temp.append(s)
        result.append(sorted(set(temp)))
for item in result:
    if(len(item) > 1):     
        for i in range(0,len(item) - 1):
            print(item[i],end = ' ')
        print(item[-1])
    else:
        print(item[0])