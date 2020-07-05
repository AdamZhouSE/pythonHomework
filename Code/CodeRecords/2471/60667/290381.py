t = int(input())
for i in range(t):
    s = input()
    length = len(s)
    for j in range(int(length/2)):
        check = True
        if s[j] == '(':
            if s[length - j-1] != ')':
                check = False
                break
        elif s[j] == '[':
            if s[length - j-1] != ']':
                check = False
                break
        elif s[j] == '{':
            if s[length - j-1] != '}':
                check = False
                break
    if check:
        print('balanced')
    else:
        print('not balanced')
            