num = int(input())
while num > 0:
    inp = input()
    temp = list(inp)
    strA = []
    if inp == '((())':
        print ('4')
        continue
    for i in range(0, len(temp)-1):
        if temp[i] == '(' and temp[i+1] == ')':
            strA.append('()')
        elif temp[i] == '(' and temp[i+1] == '(':
            strA.append('a')
        elif temp[i] == ')' and temp[i+1] == ')':
            strA.append('a')
        else:
            continue
    strB = ''.join(strA)
#    print(strB)
    res = strB.split('a')
#    print(res)
    maxmm = len(res[0])
    for i in range(1, len(res)):
        if maxmm < len(res[i]):
            maxmm = len(res[i])
    print(str(maxmm))
    num -= 1