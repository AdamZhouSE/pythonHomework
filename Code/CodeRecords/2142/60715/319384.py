t = int(input())
for test in range(t):
    list1 = []
    count = 0
    stack = []
    for i in input():
        if i == '(' or i == ')':
            list1.append(i)
    for i in range(len(list1)):
        if list1[i] == '(':
            count += 1
            stack.append(count)
            print(stack[-1], end = ' ')
        else:
            if stack[-1] == 1:
                print(1,end=' ')
            else:
                print(stack[-1],end = ' ')
                stack.pop()

    print()
    