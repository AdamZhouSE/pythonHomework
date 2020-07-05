nStr=input()


def reorderedPowerOf2(nStr):
    nStr=''.join(sorted(nStr))
    nLen = len(nStr)
    for i in range(32):
        numStr = str(2 ** i)
        if len(numStr) > nLen:
            return 'false'
        numStr=''.join(sorted(numStr))
        if numStr==nStr:
            return 'true'
    return 'false'


print(reorderedPowerOf2(nStr))