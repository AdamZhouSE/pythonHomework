questNum = int(input())

for quest in range(questNum):
    s = input()
    
    numStr = ''
    ans = 0
    start = True
    for i in range(len(s)):
        num1 = 0
        num2 = 0
        if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            numStr += s[i]
        else:
            if numStr != '':
                if start:
                    num1 = numStr[:-1]
                    num2 = numStr[-1]
                else:
                    num1 = numStr
                numStr = ''


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
