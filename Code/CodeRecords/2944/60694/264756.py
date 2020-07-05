s = input()
stack = []
for ch in s:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if len(stack) == 0:
            print("NO")
            exit()
        stack.pop()
print(len(stack) == 0)
