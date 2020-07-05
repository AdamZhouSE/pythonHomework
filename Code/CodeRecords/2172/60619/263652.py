def pop():
    result = stack[len(stack) - 1]
    del (stack[len(stack) - 1])
    return result


t = int(input())
for ind in range(t):
    string = input()
    stack = []
    for i in string:
        if i == "+" or i == "-":
            if len(stack) == 0 or (stack[len(stack) - 1] != "*" and stack[len(stack) - 1] != "/" and stack[len(stack)-1]!="^"):
                stack.append(i)
            elif stack[len(stack) - 1] == "*" or stack[len(stack) - 1] == "/" or stack[len(stack)-1]=="^":
                while len(stack) > 0 and stack[len(stack) - 1] != "+" and stack[len(stack) - 1] != "-" and stack[len(stack)-1] != "(":
                    print(pop(), end="")
                stack.append(i)
        elif i == "*" or i == "/" or i == "^":
            stack.append(i)
        elif i == "(":
            stack.append("(")
        elif i == ")":
            s = pop()
            while s != "(":
                print(s, end="")
                s = pop()
            
        else:
            print(i, end="")
    while len(stack) != 0:
        print(pop(), end="")
    print()
