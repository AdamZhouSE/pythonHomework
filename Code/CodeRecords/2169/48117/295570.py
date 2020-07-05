questNum = int(input())

for quest in range(questNum):
    s = input()
    numStack = []
    numStr = ''
    ans = 0
    start = True
    for i in range(len(s)):
        if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            numStr += s[i]
        else:
            if numStr != '':
                if start:
                    numStack.append(numStr[:-1])
                    numStack.append(numStr[-1])
                else:
                    numStack.append(numStr)
                numStr = ''

            if start:
                num2 = int(numStack.pop())
                num1 = int(numStack.pop())
            else:
                num1 = numStack.pop()

            operator = s[i]
            if operator == '*':
                if start:
                    ans = num1 * num2
                    start = False
                else:
                    ans *= num1
            elif operator == '+':
                if start:
                    ans = num1 + num2
                    start = False
                else:
                    ans += num1
            elif operator == '-':
                if start:
                    ans = num1 - num2
                    start = False
                else:
                    ans -= num1
            elif operator == '/':
                if start:
                    ans = num1 / num2
                    start = False
                else:
                    ans /= num1

    print(ans)
