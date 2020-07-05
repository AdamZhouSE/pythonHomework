def match(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')' and stack[len(stack)-1] == '(':
            stack.pop(len(stack)-1)
        elif s[i] == ']' and stack[len(stack)-1] == '[':
            stack.pop(len(stack)-1)
        elif s[i] == '}' and stack[len(stack)-1] == '{':
            stack.pop(len(stack)-1)
        else:
            return "not balanced"

    if len(stack) != 0:
        return "not balanced"
    else:
        return "balanced"


n = int(input())
string = []

for i in range(n):
    string.append(input())

for i in range(n):
    print(match(string[i]))