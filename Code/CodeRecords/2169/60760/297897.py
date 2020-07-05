def func(arr:list):
    stack=[]
    for i in arr:
        if i=='-' or i=='+' or i=='*' or i=='/':
            if i=='-':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(b-a)
            if i=='+':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(b+a)
            if i=='*':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(b*a)
            if i=='/':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                stack.append(b/a)
        else:
            stack.append(int(i))
    return stack[-1]

tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(list(input()))
for i in lists:
    print(func(i))