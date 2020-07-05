t = int(input())

inli = []
for i in range(t):
    inli.append(input())

for i in range(t):
    stack = []
    isOK = True
    for j in inli[i]:
        # print(j)
        if j == "{" or j == "[" or j == "(":
            stack.append(j)
        elif j == "}" or j == "]" or j == ")":
            if len(stack) == 0: 
                isOK = False
                break
            left = stack.pop()
            if j == "}" and left == "{": continue
            if j == "]" and left == "[": continue
            if j == ")" and left == "(": continue
            isOK = False
            break

    if len(stack) != 0: isOK = False
    if isOK: print("balanced")
    else: print("not balanced")