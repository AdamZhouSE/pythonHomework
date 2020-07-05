for test in range(0, int(input())):
    result = 'balanced'
    string = input()
    s1, s2, s3 = [], [], []
    for x in string:
        if x == '{':
            s1.append(x)
        elif x == '}':
            if not s1:
                result = 'not balanced'
                break
            else:
                s1.pop(-1)
        elif x == '(':
            s2.append('(')
        elif x == ')':
            if not s2:
                result = 'not balanced'
                break
            else:
                s2.pop(-1)
        elif x == '[':
            s3.append('[')
        elif x == ']':
            if not s3:
                result = 'not balanced'
            else:
                s3.pop(-1)
    if not s1 and not s2 and not s3 and result == 'balanced':
        print(result)
    else:
        print('not balanced')