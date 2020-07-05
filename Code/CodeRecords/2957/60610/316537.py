def W(s):
    count = 1
    result = []
    while(count <= len(s)):
        i = 0
        while(i + count <= len(s)):
            result.append(s[i:i+count])
            i += 1
        count += 1
    result = list(set(result))
    return result

def isVaild(string):
    pre = string[0]
    situation = 1
    for x in range(1,len(string)):
        if(pre!=string[x]):
            situation += 1
            pre = string[x]
    if(situation >= 3):
        return False
    else:
        return True
string = input()
temp = W(string)
count = 0
for m in temp:
    if(isVaild(m)):
        count += 1
print(count)
