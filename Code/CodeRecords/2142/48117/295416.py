questNum = int(input())

for quest in range(questNum):
    s = input()
    stack = []
    
    index = 0
    for i in range(len(s))
        if s[i] == '(':
            stack.append('(')
            index += 1
            print(index, end=' ')
        elif s[i] == ')':
            stack.pop()
            print(index, end=' ')
            index += 1
            
    print()