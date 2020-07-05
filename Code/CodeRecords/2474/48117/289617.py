questNum = int(input())

for quest in range(questNum):
    s = input()
    stack = []

    sum = 0
    for i in range(len(s)):
        temp = s[i]
        if temp == '(':
            stack.append('(')
        elif temp == ')':
            if len(stack) != 0:
                stack.pop()
                sum += 2

    print(sum)