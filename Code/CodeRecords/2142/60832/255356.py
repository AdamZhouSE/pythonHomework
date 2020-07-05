All = int(input())

for q in range(0, All):
    string = input()
    length = len(string)

    stack=[]
    index=1
    for i in range(0, length):
        if string[i] == '(':
            stack.append(index)
            print(index,end=' ')
            index+=1

        elif string[i] == ')':
            print(stack.pop(), end=' ')
    print()



