def push(s):
    stack.append(s)


def pop():
    result = stack[len(stack) - 1]
    del (stack[len(stack) - 1])
    return result


t = int(input())
for ind in range(t):
    string = input().replace(" ","")
    stack = []
    for i in range(len(string)):
        if "0" <= string[i] <= "9":
            push(int(string[i]))
        else:
            a1 = pop()
            a2 = pop()
            if string[i] == "+":
                push(a1+a2)
            elif string[i] == "-":
                push(a2-a1)
            elif string[i] == "*":
                push(a2*a1)
            else:
                push(a2/a1)
    print(stack[0])
