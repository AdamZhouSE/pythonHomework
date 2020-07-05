stack = []
def pop():
    global stack
    a = stack[len(stack) - 1]
    stack = stack[:len(stack) - 1]
    return a
def push(x):
    stack.append(x)
    
for t in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i].isnumeric():
            push(ord(s[i]) - 48)
        else:
            b = pop()
            a = pop()
            c = 0
            if s[i] == '+': c = a + b
            if s[i] == '-': c = a - b
            if s[i] == '*': c = a * b
            if s[i] == '/': c = a // b
            push(c)
    print(pop())