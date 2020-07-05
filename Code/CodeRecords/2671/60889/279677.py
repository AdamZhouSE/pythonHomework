def endWith01(length):
    if length == 1:
        return 1
    else:
        return endWith0(length-1)

def endWith0(length):
    if length == 1:
        return 1
    else:
        return 2**(length-1)-with11In(length-1)
    

def with11In(length):
    if length == 1:
        return 0
    else:
        return 2 * with11In(length-1) + endWith01(length-1)
    
numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    print(with11In(num))