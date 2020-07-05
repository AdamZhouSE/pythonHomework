
num=int(input())
testList=[]
for i in range(num):
    testList.append(input())
for i in range(num):
    test=list(testList[i])
    stack=[]
    left=0
    right=0
    for x in test:
        if x=='{' or x=='(' or x=='[':
            left+=1
        else:
            right+=1
    if left!=right:
        print("not balanced")
    else:
        for x in test:
            if x == '{' or x == '(' or x == '[':
                stack.append(x)
            if x == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
            if x == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
            if x == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
        if len(stack) != 0:
            print("not balanced")
        else:
            print("balanced")