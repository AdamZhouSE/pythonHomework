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

def find(string):
    result = 1
    if len(string) == 1:
        return result
    for length in range(1,len(string)+1):
        for start in range(0,len(string) - length+1):
            sub = string[start:start+length]
            if isdubble(string,sub):
                result = max(result,find(sub)+1)
    return result


string = input()
print(find(string))
