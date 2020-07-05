questNum = int(input())

for quest in range(questNum):
    s = input()
    stack = []
    
    reverse = 0
    for i in range(s):
        if i == '{':
            stack.append('{')
        elif i == '}':
            if len(stack) == 0:
                reverse += 1
                stack.append('{')
    
    if len(stack) != 0:
        reverse += len(stack) // 2
    
    print(reverse)