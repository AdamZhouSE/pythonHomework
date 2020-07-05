ex = input()
stack = []
flag = True
for i in range(0, len(ex)):
    if ex[i] == "(":
        stack.append(0)
    elif ex[i] == ")":
        if len(stack) == 0:
            flag = False
            break
        else:
            stack.remove(stack[0])
if flag and len(stack) == 0:
    print("YES", end="")
else:
    print("NO", end="")