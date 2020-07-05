def func(s:str):
    stack=[-1]
    res=0
    for i,x in enumerate(s):
        if x=='(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                res=max(res,i-stack[-1])
            else:
                stack.append(i)
    return res

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(input())
for i in lists:
    print(func(i))