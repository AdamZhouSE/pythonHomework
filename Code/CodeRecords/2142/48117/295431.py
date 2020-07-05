questNum = int(input())

for quest in range(questNum):
    s = input()
    stack = []
    number = []
    index = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            index += 1
            number.append(index)
            print(index, end=' ')
        elif s[i] == ')':
            stack.pop()
            print(number.pop(), end=' ')
            

    print()