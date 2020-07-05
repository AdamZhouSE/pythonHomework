def priority(sign):
    dict = {'(':0 , '#':-1 , '+':1 , '-':1 , '*':2 , '/':2 , '^':3 , ')':4}
    return dict[sign]

def do(infix):
    sign = ['#']
    stack = []
    for x in infix:
        if ord('a')<=ord(x)<=ord('z') or ord('A')<=ord(x)<=ord('Z'):
            stack.append(x)
        else:
            if x == '(':
                sign.append(x)
            elif x == ')':
                topsign = sign.pop()
                while topsign != '(':
                    stack.append(topsign)
                    topsign = sign.pop()
            else:
                while priority(x) <= priority(sign[-1]):
                    stack.append(sign.pop())
                sign.append(x)
    del sign[0]
    for i in sign:
        stack.append(sign.pop())
    pos = ''.join(stack)
    return pos


test = int(input())
for i in range(test):
    infix = input()
    print(do(infix))