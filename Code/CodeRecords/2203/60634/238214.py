def findAllPrefix(str):
    result = []
    i = 1
    while i < len(str)+1:
        result.append(str[0:i])
        i += 1
    return result


def compareStr(s1,s2):
    i = 0
    size = min(len(s1) , len(s2))
    while i <= size:
        if i == size:
            if len(s1) > len(s2):
                return 1
            elif len(s1) < len(s2):
                return 2
            else:  # len(s1) == len(s2):
                return 0
        if s1[i] < s2[i]:
            return 1
        elif s1[i] > s2[i]:
            return 2
        i += 1


#main-----
source = input()
prefix = findAllPrefix(source)
for str in prefix:
    mysterious = 0
    length = 2
    while length < len(str):
        i = 0
        while (i + length - 1) < len(str):
            j = i + 1
            while j <= i + length -1:
                if compareStr(str[i:i+length],str[j:j+length])==0:
                    mysterious += length
                j += 1
            i += 1
        length += 1
    print(mysterious)