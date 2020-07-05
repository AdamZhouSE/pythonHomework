questNum = int(input())

for quest in range(questNum):
    s = input()
    stack = []

    reverse = 0
    for i in range(len(s)):
        if s[i] == '{':
            stack.append('{')
        elif s[i] == '}':
            if len(stack) == 0:
                reverse += 1
                stack.append('{')
            else:
                stack.pop()

    if len(stack) != 0:
        if len(stack) % 2 != 0:
            reverse = -1
        else:
            reverse += len(stack) // 2

    print(reverse)