t=int(input())
for k in range(0,t):
    strr=list(input())
    stack=[]
    h=0
    balanced=True
    for c in strr:
        if (c=='{')or(c=='(')or(c=='['):
            stack.append(c)
            h+=1
        else:
            if h==0:
                balanced=False
                break
            else:
                top=stack.pop()
                h-=1
                if c=='}':
                    if top!='{':
                        balanced=False
                        break
                elif c==']':
                    if top!='[':
                        balanced=False
                        break
                elif c==')':
                    if top!='(':
                        balanced=False
                        break
    if balanced=False:
        print("not balanced")
    else:
        print("balanced")
                    