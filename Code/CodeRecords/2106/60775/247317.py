'''
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
输入: (10+(4+5+2)-3)+(6+8)
输出: 32
'''

def make_list(str):
    '''对表达式进行词法分析，将各个成分分离,返回一个列表'''
    result = []
    p = 0
    while p < len(str):
        if str[p] == ' ':
            p += 1
        elif ord('0') <= ord(str[p]) <= ord('9'):
            num = str[p]
            p += 1
            while p < len(str) and ord('0') <= ord(str[p]) <= ord('9'):
                num += str[p]
                p += 1
            result.append(num)
        else:
            result.append(str[p])
            p+=1
    return result

def priority(sign):
    if sign == '#':
        return 0
    elif sign == '+' or sign == '-':
        return 1
    elif sign == '(' or sign == ')':
        return -2
    else:
        print("Error")
        return -1


posfix = []
sign = ['#']
exp_str = input()
exp = make_list(exp_str)

#中缀→后缀
for e in exp:
    if e == '(':
        sign.append(e)
    elif e.isdigit():
        posfix.append(e)
    elif e == '+' or e == '-':
        while priority(e) <= priority(sign[-1]):
            posfix.append(sign.pop(-1))
        sign.append(e)
    elif e == ')':
        while sign[-1] != '(':
            posfix.append(sign.pop())
        sign.pop()
while len(sign) > 1:
    posfix.append(sign.pop())

#后缀求值
result = []
while len(posfix) >= 1 :
    e = posfix.pop(0)
    if e.isdigit():
        result.append(int(e))
    elif e == '+':
        result.append(result.pop() + result.pop())
    elif e == '-':
        result.append(result.pop(-2) - result.pop())
print(result[0])
