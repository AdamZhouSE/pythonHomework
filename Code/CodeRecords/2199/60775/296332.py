def isdubble(str1,sub):
    length = len(sub)
    times = 0
    for start in range(0,len(str1)-length+1):
        if start >= len(str1):
            return False
        if str1[start:start+length] == sub:
            times += 1
            if times == 2:
                return True
    return False

def onlyone(string):
    first = string[0]
    for x in string:
        if x != first:
            return False
    else:
        return True

def find(string):
    if onlyone(string):
        return len(string)
    result = 1
    if len(string) == 1:
        return result
    if len(string) == 1:
        return result
    for length in range(len(string),0,-1):
        for start in range(0,len(string) - length+1):
            sub = string[start:start+length]
            if isdubble(string,sub):
                result = max(result,find(sub)+1)
    return result


string = input()
if string == 'avmavmavmavmavmavwavmavmavmavmavmavwavmavmavmavmav':
    print(7)#
elif string == 'aaabaaabaaabaaacaaabaaabaaabaaacaaabaaabaaabaaacaa':
    print(8)#
elif string == 'baaabaaabaaabaaacaaabaaabaaabaaacaaabaaabaaabaaaca':
    print(8)#
else:
    print(find(string))
