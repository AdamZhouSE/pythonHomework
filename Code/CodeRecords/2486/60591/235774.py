def isValid(string):
    if(string[-1] in "0123456789"):
        return True
    return False

def run(string):
    stack = []
    temStr = ""
    for temp in string:
        if(temp =='['):
            stack.append(temStr)
            temStr = ""
            continue
        elif (temp == "]"):
            a = stack.pop()
            while(not isValid(a)):
                temStr = a + temStr
                a = stack.pop()
            temStr = temStr * eval(a[-1])
            if(len(a)>=2):
                stack.append(a[0:-1])
            stack.append(temStr)
            temStr = ""
            continue
        else:
            if(temp==" "):
                continue
            else:
                temStr += temp
    print(stack.pop())

n = eval(input())
while( n != 0):
    n = n - 1
    run(input())