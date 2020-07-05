
import re
def convert(s):
    level = {}

    level['('] = 0

    level['+'] = 1

    level['-'] = 1

    level['*'] = 2

    level['/'] = 2

    output = []

    opStack = []

    list = s.split()

    for i in list:

        if re.match(r'^\d+$',i):

            output.append(i)

        elif i == '(':

            opStack.append(i)

        elif i == ')':

            top = opStack.pop()

            while top != '(':

                output.append(top)

                top = opStack.pop()

        elif i in '+-*/':

            while opStack and \

                    (opStack[-1] >= i):

                output.append(opStack.pop())

            opStack.append(i)

        else:
            raise Exception('meet a unexpected operator "%s"' % (i,))
    while opStack:

        output.append(opStack.pop())
    return output

 

def cal(a,b,op):

    if op=='+':

        return a+b

    elif op=='-':

        return a-b

    elif op=='*':

        return a*b

    elif op=='/':

        return a/b

    else:

        raise Exception('meet a unexpected operator "%s" ' % (op,))

def numEval(list):

    op = []

    for i in list:

        if re.match(r'^\d+$',i):

            op.append(int(i))

        elif i in '/*-+':

            a = op.pop()

            b = op.pop()

            op.append(cal(a,b,i))

        else:

            raise Exception('meet a unexpected operator "%s" ' % i)

    return op[0]

t = int(input())
for te in range(t):
    a=input()
    print(' '.join(convert(a)))
