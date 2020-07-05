def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def isValid(l):
    s = sum(l)
    if s % 2 != 0:
        return False
    
    for i in range (len(l)):
        tmp = l[i]
        if tmp > s - tmp:
            return False
    return True

input()
l = getInput()
t = isValid(l)
if t == True:
    print('YES')
else:
    print('NO')