All = int(input())

for q in range(0, All):
    s=input()
    stack=[]
    ans=0
    for c in s:
        if c=='(':
            stack.append(c)
        elif c==')':
            if len(stack)!=0:
                ans+=2
                stack.pop()
    print(ans)