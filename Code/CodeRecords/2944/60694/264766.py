s = input()
stack = []
for ch in s:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if len(stack) == 0:
            print("NO", end="")
            exit()
        stack.pop()
if len(stack) == 0:
    print("YES", end="")
else:
    print("NO", end="")
