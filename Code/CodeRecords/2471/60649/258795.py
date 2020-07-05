T=int(input())
for i in range(T):
    s=input()
    stack=[]
    left=['(','[','{']
    right=[')',']','}']
    for c in s:
        if c in left:
            stack.append(c)
        else:
            if c==')':
                if '(' in stack:
                    stack.remove('(')
                else:
                    print("not balanced")
                    break
            if c==']':
                if '[' in stack:
                    stack.remove('[')
                else:
                    print("not balanced")
                    break
            if c=='}':
                if '{' in stack:
                    stack.remove('{')
                else:
                    print("not balanced")
                    break
    else:
        if len(stack)==0:
            print("balanced")
        else:
            print("not balanced")