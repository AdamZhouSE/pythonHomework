def calOnce(ch,stack):
    b = stack.pop()
    a = stack.pop()
    if ch == '+':
        stack.append(a + b)
    elif ch == '-':
        stack.append(a - b)
    else:
        print("symbol not defined")
        

def ip(ch):
    if ch == '(':
        return 1
    elif ch == '#':
        return 0
    elif ch == '+':
        return 2
    elif ch == '-':
        return 2
def op(ch):
    if ch == '(':
        return 99
    else:
        return ip(ch)

def cal(expre):
    symStack = ['#']
    numStack = []
    i = 0
    while True:
        if expre[i] == '#':
            while len(symStack) > 1:
                calOnce(symStack.pop(),numStack)
            break
        elif expre[i] <= '9' and expre[i] >= '0':
            numStack.append(int(expre[i]))
        elif expre[i] == ')':
            temp = symStack.pop()
            while temp != '(':
                calOnce(temp,numStack)
                temp = symStack.pop()
        elif expre[i] == ' ':
            i += 0
            # nothing to do
        else:
            temp = symStack.pop()
            while ip(temp) >= op(expre[i]):
                calOnce(temp,numStack)
                temp = symStack.pop()
            symStack.append(temp)
            symStack.append(expre[i])      
        i += 1
    return numStack[0]

#main-----
expre = input()
expre += "#"
print(cal(expre))