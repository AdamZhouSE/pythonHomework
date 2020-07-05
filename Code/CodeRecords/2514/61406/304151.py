def substring(sub,source):
    result = []
    for x in sub:
        try:
            index=source.find(x)
        except ValueError:
            return False
        result.append(index)
        source = source[:index]+source[index+1:]
    result1 = result.copy()
    result.sort()
    if result1==result:
        return True
    else:
        return False


sub = input()
source = input()
print(substring(sub,source))

