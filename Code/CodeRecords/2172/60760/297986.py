def func(arr:list):
    postfix=''
    stack=['#']
    for i in arr:
        if i=='-' or i=='+' or i=='/' or i=='*' or i=='^' or i=='(' or i==')':
            if i!=')':
                while com(stack[-1],i):
                    postfix+=stack.pop()
                stack.append(i)
            else:
                while stack[-1]!='(':
                    postfix+=stack.pop()
                stack.pop()
        else:
            postfix+=i
    while len(stack)>1:
        postfix+=stack.pop()

    return postfix

def com(a:str,b:str):
    if a=='#':
        return False
    if b=='(':
        return False
    if a=='^':
        if b=='(':
            return False
        else:
            return True
    if a=='*' or a=='/':
        if b=='^':
            return False
        else:
            return True
    if a=='+' or a=='-':
        if b=='+' or b=='-':
            return True
        else:
            return False


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    lists.append(list(input()))
for i in lists:
    print(func(i))
